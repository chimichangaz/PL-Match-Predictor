import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
from sklearn.impute import SimpleImputer


# Load the combined dataset
data = pd.read_csv('C:/Users/abc/ok/Datsets/combined_data.csv')

# Define features and target
features = [
    'HomeTeam',
    'AwayTeam',
    'HomeTeam_Goals_Scored_Last_5',
    'AwayTeam_Goals_Scored_Last_5',
    'HomeTeam_Goals_Conceded_Last_5',
    'AwayTeam_Goals_Conceded_Last_5',
    'HomeTeam_Wins_Last_5',
    'AwayTeam_Wins_Last_5',
    'HomeTeam_Draws_Last_5',
    'AwayTeam_Draws_Last_5',
    'HomeTeam_Losses_Last_5',
    'AwayTeam_Losses_Last_5',
    'B365H',
    'B365D',
    'B365A',
    'Time',
    'Referee'
]
target = 'FTR'
source = pd.read_csv('C:/Users/HP/Documents/Datsets/combined_data.csv')
# Initialize the imputer for numerical values
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'

# Apply imputer to the features with missing values
source[['HomeTeam_Wins_Last_5', 'AwayTeam_Wins_Last_5',
      'HomeTeam_Draws_Last_5', 'AwayTeam_Draws_Last_5',
      'HomeTeam_Losses_Last_5', 'AwayTeam_Losses_Last_5']] = imputer.fit_transform(
          source[['HomeTeam_Wins_Last_5', 'AwayTeam_Wins_Last_5',
                'HomeTeam_Draws_Last_5', 'AwayTeam_Draws_Last_5',
                'HomeTeam_Losses_Last_5', 'AwayTeam_Losses_Last_5']]
      )
# Define features and target
X = data[features]
y = data[target]

# Process the 'Time' column: convert 'HH:MM' format to minutes from midnight
X['Time'] = X['Time'].str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))

# Encode 'Referee' column
le_referee = LabelEncoder()
X['Referee'] = le_referee.fit_transform(X['Referee'])

# Initialize LabelEncoders for categorical features
le_home = LabelEncoder()
le_away = LabelEncoder()

# Encode HomeTeam and AwayTeam as numerical values
X['HomeTeam'] = le_home.fit_transform(X['HomeTeam'])
X['AwayTeam'] = le_away.fit_transform(X['AwayTeam'])

# Encode FTR (Full Time Result) as target variable
y = y.map({'H': 1, 'D': 0, 'A': 2})

# Standardize B365H, B365D, B365A features using StandardScaler
scaler = StandardScaler()
X[['B365H', 'B365D', 'B365A']] = scaler.fit_transform(X[['B365H', 'B365D', 'B365A']])

# Initialize the model
model = RandomForestClassifier(n_estimators=46, random_state=42, class_weight='balanced')

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=666)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'model222.pkl')

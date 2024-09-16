from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the combined dataset
data = pd.read_csv('C:/Users/HP/Downloads/combined_data.csv')

# Define features and target
features = ['HomeTeam', 'AwayTeam', 'HomeTeam_Goals_Scored_Last_5', 'AwayTeam_Goals_Scored_Last_5',
            'HomeTeam_Goals_Conceded_Last_5', 'AwayTeam_Goals_Conceded_Last_5',
            'HomeTeam_Wins_Last_5', 'AwayTeam_Wins_Last_5',
            'HomeTeam_Draws_Last_5', 'AwayTeam_Draws_Last_5',
            'HomeTeam_Losses_Last_5', 'AwayTeam_Losses_Last_5','B365H', 'B365D', 'B365A']
target = 'FTR'

# Define features and target
X = data[features]
y = data[target]  # 'FTR' column as target

# Initialize LabelEncoders for categorical features
le_home = LabelEncoder()
le_away = LabelEncoder()

# Encode HomeTeam and AwayTeam as numerical values
X.loc[:, 'HomeTeam'] = le_home.fit_transform(X['HomeTeam'])
X.loc[:, 'AwayTeam'] = le_away.fit_transform(X['AwayTeam'])
# Encode FTR (Full Time Result) as target variable
y = y.map({'H': 1, 'D': 0, 'A': 2})

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42,class_weight='balanced')

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=666)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

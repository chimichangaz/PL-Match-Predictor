from sklearn.impute import SimpleImputer
import pandas as pd
source = pd.read_csv('C:/Users/HP/Downloads/combined_data.csv')
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

#This class checks for NULL values and andy empty spaces in the datasets

import pandas as pd
source = pd.read_csv('C:/Users/HP/Downloads/combined_data.csv')
source.info()
check = source.isnull().sum()
print(check)
# identified null values in 6 fields
print(source[['HomeTeam_Wins_Last_5', 'AwayTeam_Wins_Last_5',
            'HomeTeam_Draws_Last_5', 'AwayTeam_Draws_Last_5',
            'HomeTeam_Losses_Last_5', 'AwayTeam_Losses_Last_5']].isnull().sum())

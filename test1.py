import pandas as pd
pl2122 = pd.read_csv("C:/Users/HP/Downloads/p21-22.csv")
pl2223 = pd.read_csv("C:/Users/HP/Downloads/p22-23.csv")
pl2324 = pd.read_csv("C:/Users/HP/Downloads/p23-24.csv")
# Step 1: Sort by date and group by teams to calculate rolling averages
# Load datasets
data_21_22 = pd.read_csv('C:/Users/HP/Downloads/p21-22.csv')
data_22_23 = pd.read_csv('C:/Users/HP/Downloads/p22-23.csv')
data_23_24 = pd.read_csv('C:/Users/HP/Downloads/p23-24.csv')

# Combine datasets into one DataFrame
combined_data = pd.concat([data_21_22, data_22_23, data_23_24], ignore_index=True)

# Sort by date to maintain chronological order if the date column exists
combined_data = combined_data.sort_values(by='Date')  # Replace 'Date' with the actual date column name if necessary

combined_data = combined_data.sort_values(by='Date')

# Rolling averages for goals scored and conceded (using a 5-match window)
combined_data['HomeTeam_Goals_Scored_Last_5'] = combined_data.groupby('HomeTeam')['FTHG'].transform(lambda x: x.rolling(5, closed='left').mean())
combined_data['AwayTeam_Goals_Scored_Last_5'] = combined_data.groupby('AwayTeam')['FTAG'].transform(lambda x: x.rolling(5, closed='left').mean())

combined_data['HomeTeam_Goals_Conceded_Last_5'] = combined_data.groupby('HomeTeam')['FTAG'].transform(lambda x: x.rolling(5, closed='left').mean())
combined_data['AwayTeam_Goals_Conceded_Last_5'] = combined_data.groupby('AwayTeam')['FTHG'].transform(lambda x: x.rolling(5, closed='left').mean())

# Step 2: Calculate win/loss streaks for both home and away teams
combined_data['HomeTeam_Wins_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'H').rolling(5, closed='left').sum())
combined_data['AwayTeam_Wins_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'A').rolling(5, closed='left').sum())

combined_data['HomeTeam_Draws_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'D').rolling(5, closed='left').sum())
combined_data['AwayTeam_Draws_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'D').rolling(5, closed='left').sum())

combined_data['HomeTeam_Losses_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'A').rolling(5, closed='left').sum())
combined_data['AwayTeam_Losses_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'H').rolling(5, closed='left').sum())
print(combined_data['FTR'].unique())




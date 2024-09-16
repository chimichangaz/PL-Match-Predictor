# Import necessary libraries
import pandas as pd
import os

# Step 1: Check the current working directory to verify file location
print("Current working directory:", os.getcwd())

# Step 2: Load datasets
# Make sure the file paths are correct. You can use absolute or relative paths
data_21_22 = pd.read_csv('C:/Users/HP/Downloads/p21-22.csv')
data_22_23 = pd.read_csv('C:/Users/HP/Downloads/p22-23.csv')
data_23_24 = pd.read_csv('C:/Users/HP/Downloads/p23-24.csv')

# Step 3: Combine datasets into one DataFrame
# Ignore the index to avoid duplicate indices from different seasons
combined_data = pd.concat([data_21_22, data_22_23, data_23_24], ignore_index=True)

# Step 4: Sort by date to maintain chronological order (assuming there is a 'Date' column)
# Replace 'Date' with the actual name of your date column if it's different
combined_data = combined_data.sort_values(by='Date')

# Step 5: Calculate rolling averages for goals scored and conceded over the last 5 matches
# Ensure we use a window of 5 matches to capture recent team form
combined_data['HomeTeam_Goals_Scored_Last_5'] = combined_data.groupby('HomeTeam')['FTHG'].transform(lambda x: x.rolling(5, closed='left').mean())
combined_data['AwayTeam_Goals_Scored_Last_5'] = combined_data.groupby('AwayTeam')['FTAG'].transform(lambda x: x.rolling(5, closed='left').mean())

combined_data['HomeTeam_Goals_Conceded_Last_5'] = combined_data.groupby('HomeTeam')['FTAG'].transform(lambda x: x.rolling(5, closed='left').mean())
combined_data['AwayTeam_Goals_Conceded_Last_5'] = combined_data.groupby('AwayTeam')['FTHG'].transform(lambda x: x.rolling(5, closed='left').mean())

# Step 6: Calculate win/loss/draw streak for both home and away teams over the last 5 matches
# Wins: Home team (FTR == 'H'), Away team (FTR == 'A')
# Draws: (FTR == 'D')
# Losses: Opposite of wins (Home loss if FTR == 'A', Away loss if FTR == 'H')
combined_data['HomeTeam_Wins_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'H').rolling(5, closed='left').sum())
combined_data['AwayTeam_Wins_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'A').rolling(5, closed='left').sum())

combined_data['HomeTeam_Draws_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'D').rolling(5, closed='left').sum())
combined_data['AwayTeam_Draws_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'D').rolling(5, closed='left').sum())

combined_data['HomeTeam_Losses_Last_5'] = combined_data.groupby('HomeTeam')['FTR'].transform(lambda x: (x.shift() == 'A').rolling(5, closed='left').sum())
combined_data['AwayTeam_Losses_Last_5'] = combined_data.groupby('AwayTeam')['FTR'].transform(lambda x: (x.shift() == 'H').rolling(5, closed='left').sum())

# Step 7: Preview the dataset with the new columns to ensure the calculations were applied correctly
print(combined_data.tail())  # Shows the last 5 rows of the entire DataFrame
# Save the combined DataFrame to a CSV file



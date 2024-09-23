from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('model_resampled.pkl')

# Load the dataset to get the team names
data = pd.read_csv('C:/Users/ok/abc/Datsets/combined_data.csv')

# Initialize and fit LabelEncoders
le_home = LabelEncoder()
le_away = LabelEncoder()
le_home.fit(data['HomeTeam'])
le_away.fit(data['AwayTeam'])

# Serve team names to React frontend
@app.route('/teams', methods=['GET'])
def get_teams():
    teams = sorted(data['HomeTeam'].unique())
    return jsonify({'teams': teams})

# API endpoint for predictions (used by React frontend)
@app.route('/', methods=['POST'])
def predict():
    try:
        request_data = request.get_json()
        home_team = request_data['home_team']
        away_team = request_data['away_team']

        # Retrieve the latest statistics for the selected teams
        home_team_data = data[data['HomeTeam'] == home_team].tail(1)
        away_team_data = data[data['AwayTeam'] == away_team].tail(1)

        # Safeguard against empty results
        if home_team_data.empty or away_team_data.empty:
            return jsonify({'error': 'No data found for the selected teams'}), 400

        # Prepare the input data
        input_data = pd.DataFrame({
            'HomeTeam': [home_team],
            'AwayTeam': [away_team],
            'HomeTeam_Goals_Scored_Last_5': [home_team_data['HomeTeam_Goals_Scored_Last_5'].values[0]],
            'AwayTeam_Goals_Scored_Last_5': [away_team_data['AwayTeam_Goals_Scored_Last_5'].values[0]],
            'HomeTeam_Goals_Conceded_Last_5': [home_team_data['HomeTeam_Goals_Conceded_Last_5'].values[0]],
            'AwayTeam_Goals_Conceded_Last_5': [away_team_data['AwayTeam_Goals_Conceded_Last_5'].values[0]],
            'HomeTeam_Wins_Last_5': [home_team_data['HomeTeam_Wins_Last_5'].values[0]],
            'AwayTeam_Wins_Last_5': [away_team_data['AwayTeam_Wins_Last_5'].values[0]],
            'HomeTeam_Draws_Last_5': [home_team_data['HomeTeam_Draws_Last_5'].values[0]],
            'AwayTeam_Draws_Last_5': [away_team_data['AwayTeam_Draws_Last_5'].values[0]],
            'HomeTeam_Losses_Last_5': [home_team_data['HomeTeam_Losses_Last_5'].values[0]],
            'AwayTeam_Losses_Last_5': [away_team_data['AwayTeam_Losses_Last_5'].values[0]],
            'B365H': [2.0],  # Default odds or retrieve from your dataset if available
            'B365D': [3.0],
            'B365A': [2.0],
            'Time': [0],  # Replace with actual value if available
            'Referee': [0]  # Replace with actual value if available
        })

        # Encode HomeTeam and AwayTeam
        input_data['HomeTeam'] = le_home.transform(input_data['HomeTeam'])
        input_data['AwayTeam'] = le_away.transform(input_data['AwayTeam'])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Convert prediction to result
        result = {0: 'Draw', 1: 'Home Team Wins', 2: 'Away Team Wins'}[prediction]

        return jsonify({'home_team': home_team, 'away_team': away_team, 'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

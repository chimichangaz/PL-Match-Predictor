# PL-Match-Predictor
This project uses machine learning to predict the outcomes of Premier League football matches, specifically focusing on Full-Time Results (FTR) — Home Win (H), Draw (D), or Away Win (A). The model leverages a Random Forest Classifier to make predictions based on team statistics and betting odds.
Features
Match Statistics: Historical data such as goals scored, goals conceded, wins, draws, and losses from both home and away teams' last five matches.
Betting Odds: Incorporates odds from popular betting platforms like B365 (for Home Win, Draw, and Away Win).
Feature Encoding: Categorical data like team names are label-encoded, and match outcomes (FTR) are converted to numerical values (1 for Home Win, 0 for Draw, 2 for Away Win).
Challenges & Solutions
Handling Missing Data: Imputation techniques are applied to handle null values in key statistics like recent wins, draws, and losses.
Imbalanced Classes: Addressed through oversampling and adjusting model parameters.
Model Performance: Evaluated using accuracy, precision, recall, and F1-score for each outcome class.
Potential Future Enhancements
Adding player-specific data (e.g., injuries, form).
Exploring advanced models like XGBoost or Neural Networks.
Time-series analysis to track team performance trends.
Building a user-friendly web interface for real-time predictions.

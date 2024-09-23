import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap
import './App.css';  // Custom styles for better look
import app from './firebase';

function App() {
  const [teams, setTeams] = useState([]);
  const [homeTeam, setHomeTeam] = useState('');
  const [awayTeam, setAwayTeam] = useState('');
  const [result, setResult] = useState('');

  useEffect(() => {
    async function fetchTeams() {
      const response = await fetch('http://localhost:5000/teams');
      const data = await response.json();
      setTeams(data.teams);
    }
    fetchTeams();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ home_team: homeTeam, away_team: awayTeam }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setResult(`Match: ${data.home_team} vs ${data.away_team}, Result: ${data.result}`);
    } catch (error) {
      console.error("Error:", error);
      setResult("An error occurred while fetching the prediction.");
    }
  };

  return (
    <div className="app-container d-flex align-items-center justify-content-center min-vh-100">
      <div className="card p-4 shadow-lg bg-light" style={{ width: '100%', maxWidth: '600px' }}>
        {/* Animated Premier League Logo */}
        <div className="logo-container text-center mb-4">
          <img
            src="https://upload.wikimedia.org/wikipedia/en/f/f2/Premier_League_Logo.svg"
            alt="Premier League Logo"
            className="premier-league-logo"
          />
        </div>

        <h1 className="text-center mb-4 text-primary">Premier League Match Predictor</h1>

        <form onSubmit={handleSubmit}>
          <div className="form-group mb-4">
            <label className="form-label">Home Team</label>
            <select
              value={homeTeam}
              onChange={(e) => setHomeTeam(e.target.value)}
              className="form-control form-control-lg"
            >
              <option value="">Select Home Team</option>
              {teams.map((team) => (
                <option key={team} value={team}>
                  {team}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group mb-4">
            <label className="form-label">Away Team</label>
            <select
              value={awayTeam}
              onChange={(e) => setAwayTeam(e.target.value)}
              className="form-control form-control-lg"
            >
              <option value="">Select Away Team</option>
              {teams.map((team) => (
                <option key={team} value={team}>
                  {team}
                </option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn btn-primary btn-lg w-100">Predict</button>
        </form>

        {result && <h2 className="text-center mt-4 text-success">{result}</h2>}
      </div>
    </div>
  );
}

export default App;

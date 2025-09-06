from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Replace this URL with your actual backend API endpoint hosted on Render
BACKEND_API_URL = 'https://your-backend-url.onrender.com/api/user'

@app.route('/')
def login():
    # Dummy login page (no real auth)
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Fetch user data from backend API
    try:
        response = requests.get(BACKEND_API_URL)
        response.raise_for_status()
        user_data = response.json()
    except Exception:
        # Fallback static data if backend API call fails
        user_data = {
            "name": "John Doe",
            "referralCode": "johndoe2025",
            "amountRaised": 250
        }

    return render_template('dashboard.html', user=user_data)

@app.route('/leaderboard')
def leaderboard():
    # Static leaderboard data example
    leaderboard_data = [
        {"name": "Alex", "amountRaised": 500},
        {"name": "Maria", "amountRaised": 400},
        {"name": "John Doe", "amountRaised": 250}
    ]
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == '__main__':
    app.run(debug=True)


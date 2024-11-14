from flask import Flask, render_template, request, redirect, url_for
from utils.espn_api import fetch_nfl_games, fetch_live_scores
from utils.database import load_picks, load_players, save_pick, save_player, load_leaderboard
from utils.scoring import calculate_scores

app = Flask(__name__)
players = []

@app.route('/')
def index():
    games = fetch_nfl_games()  # Fetch the current week's games
    return render_template('index.html', players=players, games=games)

@app.route('/make_picks', methods=['GET', 'POST'])
def make_picks():
    players = load_players()
    games = fetch_nfl_games()

    if request.method == 'POST':
        player_picks = request.form.to_dict()
        save_pick(player_picks)  # Save the picks in the database
        return redirect(url_for('index'))

    return render_template('picks.html', players=players, games=games)

@app.route('/leaderboard')
def leaderboard():
    players = load_players()
    leaderboard_data = load_leaderboard()
    return render_template('leaderboard.html', players=players, leaderboard=leaderboard_data)

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        # Get the player name from the form
        player_name = request.form.get('player_name')
        
        # Add the player to the list
        players.append(player_name)
        
        # Redirect to the home page or another page after adding the player
        return redirect(url_for('index'))
    
    return render_template('add_player.html')



@app.route('/update_scores')
def update_scores():
    # Fetch live scores and update weekly results
    games = fetch_live_scores()
    players = load_players()
    leaderboard = calculate_scores(games, players)
    return redirect(url_for('leaderboard'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


import json

PICKS_FILE = 'data/picks.json'
PLAYERS_FILE = 'data/players.json'
LEADERBOARD_FILE = 'data/leaderboard.json'

def load_picks():
    with open(PICKS_FILE, 'r') as f:
        return json.load(f)

def save_pick(pick_data):
    with open(PICKS_FILE, 'r+') as f:
        picks = json.load(f)
        picks.append(pick_data)
        f.seek(0)
        json.dump(picks, f, indent=4)

def load_players():
    with open(PLAYERS_FILE, 'r') as f:
        return json.load(f)

def save_player(player_data):
    with open(PLAYERS_FILE, 'r+') as f:
        players = json.load(f)
        players.append(player_data)
        f.seek(0)
        json.dump(players, f, indent=4)

def load_leaderboard():
    with open(LEADERBOARD_FILE, 'r') as f:
        return json.load(f)

def save_leaderboard(leaderboard_data):
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard_data, f, indent=4)

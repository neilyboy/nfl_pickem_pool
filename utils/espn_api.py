import requests

API_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

def fetch_nfl_games():
    response = requests.get(API_URL)
    games_data = response.json()
    games = []

    for event in games_data['events']:
        game = {
            'game_id': event['id'],
            'home_team': event['competitions'][0]['competitors'][0]['team']['displayName'],
            'away_team': event['competitions'][0]['competitors'][1]['team']['displayName'],
            'home_logo': event['competitions'][0]['competitors'][0]['team']['logo'],
            'away_logo': event['competitions'][0]['competitors'][1]['team']['logo'],
            'start_time': event['date']
        }
        games.append(game)

    return games

def fetch_live_scores():
    response = requests.get(API_URL)
    games_data = response.json()
    live_scores = []

    for event in games_data['events']:
        game_id = event['id']
        home_score = event['competitions'][0]['competitors'][0]['score']['value']
        away_score = event['competitions'][0]['competitors'][1]['score']['value']
        live_scores.append({
            'game_id': game_id,
            'home_score': int(home_score),
            'away_score': int(away_score)
        })

    return live_scores

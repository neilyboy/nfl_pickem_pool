def calculate_scores(games, picks):
    leaderboard = {}

    for player in picks:
        correct_picks = 0
        player_name = player['player_name']
        leaderboard[player_name] = {
            'correct_picks': 0,
            'tiebreaker': player.get('tiebreaker', 0)
        }

        for game in games:
            # Assume each pick contains game_id with player's selected winner
            if game['game_id'] in player and game['winner'] == player[game['game_id']]:
                correct_picks += 1

        leaderboard[player_name]['correct_picks'] = correct_picks

    # Apply tiebreakers for players tied with the most correct picks
    highest_correct = max(player['correct_picks'] for player in leaderboard.values())
    tied_players = [p for p, s in leaderboard.items() if s['correct_picks'] == highest_correct]

    if len(tied_players) > 1:
        apply_tiebreaker(leaderboard, tied_players, games)

    return leaderboard

def apply_tiebreaker(leaderboard, tied_players, games):
    monday_game_total = sum(game['home_score'] + game['away_score'] for game in games if game['day'] == "Monday")

    # Closest tiebreaker without going over
    closest_player = None
    closest_diff = float('inf')

    for player in tied_players:
        diff = abs(monday_game_total - leaderboard[player]['tiebreaker'])
        if diff < closest_diff:
            closest_diff = diff
            closest_player = player

    for player in tied_players:
        leaderboard[player]['is_winner'] = (player == closest_player)

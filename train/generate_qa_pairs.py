import pandas as pd
from pybaseball import batting_stats_bref

# # Get all of this season's batting data so far
# batting_stats = batting_stats_bref()

def generate_qa_pairs_batting():
    pairs = []
    batting_stats = pd.read_csv('data/batting_stats.csv')
        # Find the player(s) with the highest batting average
    max_ba = batting_stats['BA'].max()
    max_ba_players = batting_stats.loc[batting_stats['BA'] == max_ba, 'Name'].tolist()

    if len(max_ba_players) > 1:
        max_ba_players_str = ', '.join(max_ba_players[:-1]) + ', and ' + max_ba_players[-1]
        pairs.append({
            'question': f"Who has the highest batting average?",
            'context': f"{max_ba_players_str} all have the highest batting average of {max_ba:.3f}.",
            'answer': max_ba_players
        })
    else:
        max_ba_player = max_ba_players[0]
        pairs.append({
            'question': f"Who has the highest batting average?",
            'context': f"{max_ba_player} has the highest batting average of {max_ba:.3f}.",
            'answer': max_ba_player
        })

    # Find the player(s) with the highest batting average with at least 50 PA
    qualified_batters = batting_stats.loc[batting_stats['PA'] >= 50]
    max_ba_qualified = qualified_batters['BA'].max()
    max_ba_qualified_players = qualified_batters.loc[qualified_batters['BA'] == max_ba_qualified, 'Name'].tolist()

    if len(max_ba_qualified_players) > 1:
        max_ba_qualified_players_str = ', '.join(max_ba_qualified_players[:-1]) + ', and ' + max_ba_qualified_players[-1]
        pairs.append({
            'question': f"Who has the highest batting average with at least 50 plate appearances?",
            'context': f"{max_ba_qualified_players_str} all have the highest batting average of {max_ba_qualified:.3f} with at least 50 plate appearances.",
            'answer': max_ba_qualified_players
        })
    else:
        max_ba_qualified_player = max_ba_qualified_players[0]
        pairs.append({
            'question': f"Who has the highest batting average with at least 50 plate appearances?",
            'context': f"{max_ba_qualified_player} has the highest batting average of {max_ba_qualified:.3f} with at least 50 plate appearances.",
            'answer': max_ba_qualified_player
        })

    # Find the player(s) with the most home runs
    max_hr = batting_stats['HR'].max()
    max_hr_players = batting_stats.loc[batting_stats['HR'] == max_hr, 'Name'].tolist()

    if len(max_hr_players) > 1:
        max_hr_players_str = ', '.join(max_hr_players[:-1]) + ', and ' + max_hr_players[-1]
        pairs.append({
            'question': f"Who has the most home runs?",
            'context': f"{max_hr_players_str} all have the most home runs with {max_hr}.",
            'answer': max_hr_players
        })
    else:
        max_hr_player = max_hr_players[0]
        pairs.append({
            'question': f"Who has the most home runs?",
            'context': f"{max_hr_player} has the most home runs with {max_hr}.",
            'answer': max_hr_player
        })

    # Find the player(s) with the lowest batting average
    min_ba = batting_stats['BA'].min()
    min_ba_players = batting_stats.loc[batting_stats['BA'] == min_ba, 'Name'].tolist()

    if len(min_ba_players) > 1:
        min_ba_players_str = ', '.join(min_ba_players[:-1]) + ', and ' + min_ba_players[-1]
        pairs.append({
            'question': f"Who has the lowest batting average?",
            'context': f"{min_ba_players_str} all have the lowest batting average of {min_ba:.3f}.",
            'answer': min_ba_players
        })
    else:
        min_ba_player = min_ba_players[0]
        pairs.append({
            'question': f"Who has the lowest batting average?",
            'context': f"{min_ba_player} has the lowest batting average of {min_ba:.3f}.",
            'answer': min_ba_player
        })

    # Find the player(s) with the fewest home runs
    min_hr = batting_stats['HR'].min()
    min_hr_players = batting_stats.loc[batting_stats['HR'] == min_hr, 'Name'].tolist()

    if len(min_hr_players) > 1:
        min_hr_players_str = ', '.join(min_hr_players[:-1]) + ', and ' + min_hr_players[-1]
        pairs.append({
            'question': f"Who has the fewest home runs?",
            'context': f"{min_hr_players_str} all have the fewest home runs with {min_hr}.",
            'answer': min_hr_players
        })
    else:
        min_hr_player = min_hr_players[0]
        pairs.append({
            'question': f"Who has the fewest home runs?",
            'context': f"{min_hr_player} has the fewest home runs with {min_hr}.",
            'answer': min_hr_player
        })

    # find the player(s) with the most runs scored
    max_r = batting_stats['R'].max()
    max_r_players = batting_stats.loc[batting_stats['R'] == max_r, 'Name'].tolist()
    if len(max_r_players) > 1:
        max_r_players_str = ', '.join(max_r_players[:-1]) + ', and ' + max_r_players[-1]
        pairs.append({
            'question': f"Who has the most runs scored?",
            'context': f"{max_r_players_str} all have the most runs scored with {max_r}.",
            'answer': max_r_players
        })
    else:
        max_r_player = max_r_players[0]
        pairs.append({
            'question': f"Who has the most runs scored?",
            'context': f"{max_r_player} has the most runs scored with {max_r}.",
            'answer': max_r_player
        })

    # find the player(s) with the least runs scored
    min_r = batting_stats['R'].min()
    min_r_players = batting_stats.loc[batting_stats['R'] == min_r, 'Name'].tolist()
    if len(min_r_players) > 1:
        min_r_players_str = ', '.join(min_r_players[:-1]) + ', and ' + min_r_players[-1]
        pairs.append({
            'question': f"Who has the least runs scored?",
            'context': f"{min_r_players_str} all have the least runs scored with {min_r}.",
            'answer': min_r_players
        })
    else:
        min_r_player = min_r_players[0]
        pairs.append({
            'question': f"Who has the least runs scored?",
            'context': f"{min_r_player} has the least runs scored with {min_r}.",
            'answer': min_r_player
        })
    
    # Add additional question-answer pairs here
     # Find the player(s) with the most strikeouts
    max_strikeouts = batting_stats['SO'].max()
    max_strikeouts_players = batting_stats.loc[batting_stats['SO'] == max_strikeouts, 'Name'].tolist()

    if len(max_strikeouts_players) > 1:
        max_strikeouts_players_str = ', '.join(max_strikeouts_players[:-1]) + ', and ' + max_strikeouts_players[-1]
        pairs.append({
            'question': f"Who has the most strikeouts?",
            'context': f"{max_strikeouts_players_str} all have the most strikeouts with {max_strikeouts}.",
            'answer': max_strikeouts_players
        })
    else:
        max_strikeouts_player = max_strikeouts_players[0]
        pairs.append({
            'question': f"Who has the most strikeouts?",
            'context': f"{max_strikeouts_player} has the most strikeouts with {max_strikeouts}.",
            'answer': max_strikeouts_player
        })

    # Find the player(s) with the least strikeouts
    min_strikeouts = batting_stats['SO'].min()
    min_strikeouts_players = batting_stats.loc[batting_stats['SO'] == min_strikeouts, 'Name'].tolist()

    if len(min_strikeouts_players) > 1:
        min_strikeouts_players_str = ', '.join(min_strikeouts_players[:-1]) + ', and ' + min_strikeouts_players[-1]
        pairs.append({
            'question': f"Who has the least strikeouts?",
            'context': f"{min_strikeouts_players_str} all have the least strikeouts with {min_strikeouts}.",
            'answer': min_strikeouts_players
        })
    else:
        min_strikeouts_player = min_strikeouts_players[0]
        pairs.append({
            'question': f"Who has the least strikeouts?",
            'context': f"{min_strikeouts_player} has the least strikeouts with {min_strikeouts}.",
            'answer': min_strikeouts_player
        })

     # Find the player(s) with the most walks
    max_walks = batting_stats['BB'].max()
    max_walks_players = batting_stats.loc[batting_stats['BB'] == max_walks, 'Name'].tolist()

    if len(max_walks_players) > 1:
        max_walks_players_str = ', '.join(max_walks_players[:-1]) + ', and ' + max_walks_players[-1]
        pairs.append({
            'question': f"Who has the most walks?",
            'context': f"{max_walks_players_str} all have the most walks with {max_walks}.",
            'answer': max_walks_players
        })
    else:
        max_walks_player = max_walks_players[0]
        pairs.append({
            'question': f"Who has the most walks?",
            'context': f"{max_walks_player} has the most walks with {max_walks}.",
            'answer': max_walks_player
        })

    # Find the player(s) with the least walks
    min_walks = batting_stats['BB'].min()
    min_walks_players = batting_stats.loc[batting_stats['BB'] == min_walks, 'Name'].tolist()
    
    if len(min_walks_players) > 1:
        min_walks_players_str = ', '.join(min_walks_players[:-1]) + ', and ' + min_walks_players[-1]
        pairs.append({
            'question': f"Who has the least walks?",
            'context': f"{min_walks_players_str} all have the least walks with {min_walks}.",
            'answer': min_walks_players
        })
    else:
        min_walks_player = min_walks_players[0]
        pairs.append({
            'question': f"Who has the least walks?",
            'context': f"{min_walks_player} has the least walks with {min_walks}.",
            'answer': min_walks_player
        })

    # Find the player(s) with the least walks (considering only hitters with more than 50 plate appearances)
    min_walks = batting_stats.loc[batting_stats['PA'] > 50, 'BB'].min()
    min_walks_players = batting_stats.loc[(batting_stats['BB'] == min_walks) & (batting_stats['PA'] > 50), 'Name'].tolist()
    
    if len(min_walks_players) > 1:
        min_walks_players_str = ', '.join(min_walks_players[:-1]) + ', and ' + min_walks_players[-1]
        pairs.append({
            'question': f"Who has the least walks among hitters with more than 50 plate appearances?",
            'context': f"{min_walks_players_str} all have the least walks with {min_walks} among hitters with more than 50 plate appearances.",
            'answer': min_walks_players
        })
    else:
        min_walks_player = min_walks_players[0]
        pairs.append({
            'question': f"Who has the least walks among hitters with more than 50 plate appearances?",
            'context': f"{min_walks_player} has the least walks with {min_walks} among hitters with more than 50 plate appearances.",
            'answer': min_walks_player
        })
    
    # Find the player(s) with the most walks (considering only hitters with at least 50 plate appearances)
    max_walks = batting_stats.loc[batting_stats['PA'] >= 50, 'BB'].max()
    max_walks_players = batting_stats.loc[(batting_stats['BB'] == max_walks) & (batting_stats['PA'] >= 50), 'Name'].tolist()
    
    if len(max_walks_players) > 1:
        max_walks_players_str = ', '.join(max_walks_players[:-1]) + ', and ' + max_walks_players[-1]
        pairs.append({
            'question': f"Who has the most walks among hitters with at least 50 plate appearances?",
            'context': f"{max_walks_players_str} all have the most walks with {max_walks} among hitters with at least 50 plate appearances.",
            'answer': max_walks_players
        })
    else:
        max_walks_player = max_walks_players[0]
        pairs.append({
            'question': f"Who has the most walks among hitters with at least 50 plate appearances?",
            'context': f"{max_walks_player} has the most walks with {max_walks} among hitters with at least 50 plate appearances.",
            'answer': max_walks_player
        })
    

    return pairs


import pandas as pd

def generate_qa_pairs_pitching(pitching_data_file):
    pairs = []

    # Load the pitching data from the CSV file
    pitching_data = pd.read_csv(pitching_data_file)

    # Find the pitcher(s) with the lowest ERA
    min_era = pitching_data['ERA'].min()
    min_era_pitchers = pitching_data.loc[pitching_data['ERA'] == min_era, 'Name'].tolist()

    if len(min_era_pitchers) > 1:
        min_era_pitchers_str = ', '.join(min_era_pitchers[:-1]) + ', and ' + min_era_pitchers[-1]
        pairs.append({
            'question': f"Who has the lowest ERA?",
            'context': f"{min_era_pitchers_str} all have the lowest ERA of {min_era:.2f}.",
            'answer': min_era_pitchers
        })
    else:
        min_era_pitcher = min_era_pitchers[0]
        pairs.append({
            'question': f"Who has the lowest ERA?",
            'context': f"{min_era_pitcher} has the lowest ERA of {min_era:.2f}.",
            'answer': min_era_pitcher
        })

    # Find the pitcher with the lowest ERA that has pitched at least 25 innings
    filtered_pitchers = pitching_data[pitching_data['IP'] >= 25]
    min_era_25ip = filtered_pitchers['ERA'].min()
    min_era_25ip_pitchers = filtered_pitchers.loc[filtered_pitchers['ERA'] == min_era_25ip, 'Name'].tolist()
    
    if len(min_era_25ip_pitchers) > 1:
        min_era_25ip_pitchers_str = ', '.join(min_era_25ip_pitchers[:-1]) + ', and ' + min_era_25ip_pitchers[-1]
        pairs.append({
            'question': f"Who has the lowest ERA with at least 25 IP?",
            'context': f"{min_era_25ip_pitchers_str} all have the lowest ERA of {min_era_25ip:.2f} with at least 25 IP.",
            'answer': min_era_25ip_pitchers
        })
    else:
        min_era_25ip_pitcher = min_era_25ip_pitchers[0]
        pairs.append({
            'question': f"Who has the lowest ERA with at least 25 IP?",
            'context': f"{min_era_25ip_pitcher} has the lowest ERA of {min_era_25ip:.2f} with at least 25 IP.",
            'answer': min_era_25ip_pitcher
        })
    

    # Find the pitcher(s) with the highest ERA
    max_era = pitching_data['ERA'].max()
    max_era_pitchers = pitching_data.loc[pitching_data['ERA'] == max_era, 'Name'].tolist()

    if len(max_era_pitchers) > 1:
        max_era_pitchers_str = ', '.join(max_era_pitchers[:-1]) + ', and ' + max_era_pitchers[-1]
        pairs.append({
            'question': f"Who has the highest ERA?",
            'context': f"{max_era_pitchers_str} all have the highest ERA of {max_era:.2f}.",
            'answer': max_era_pitchers
        })
    else:
        max_era_pitcher = max_era_pitchers[0]
        pairs.append({
            'question': f"Who has the highest ERA?",
            'context': f"{max_era_pitcher} has the highest ERA of {max_era:.2f}.",
            'answer': max_era_pitcher
        })

    # Find the pitcher(s) with the highest ERA and at least 25 IP
    filtered_pitchers = pitching_data[pitching_data['IP'] >= 25]
    max_era_25ip = filtered_pitchers['ERA'].max()
    max_era_25ip_pitchers = filtered_pitchers.loc[filtered_pitchers['ERA'] == max_era_25ip, 'Name'].tolist()

    if len(max_era_25ip_pitchers) > 1:
        max_era_25ip_pitchers_str = ', '.join(max_era_25ip_pitchers[:-1]) + ', and ' + max_era_25ip_pitchers[-1]
        pairs.append({
            'question': f"Who has the highest ERA with at least 25 IP?",
            'context': f"{max_era_25ip_pitchers_str} all have the highest ERA of {max_era_25ip:.2f} with at least 25 IP.",
            'answer': max_era_25ip_pitchers
        })
    else:
        max_era_25ip_pitcher = max_era_25ip_pitchers[0]
        pairs.append({
            'question': f"Who has the highest ERA with at least 25 IP?",
            'context': f"{max_era_25ip_pitcher} has the highest ERA of {max_era_25ip:.2f} with at least 25 IP.",
            'answer': max_era_25ip_pitcher
        })

    # Find the pitcher(s) with the most losses
    max_losses = pitching_data['L'].max()
    pitchers_with_most_losses = pitching_data.loc[pitching_data['L'] == max_losses, 'Name'].tolist()
    
    if len(pitchers_with_most_losses) > 1:
        pitchers_with_most_losses_str = ', '.join(pitchers_with_most_losses[:-1]) + ', and ' + pitchers_with_most_losses[-1]
        pairs.append({
            'question': "Who has the most losses?",
            'context': f"{pitchers_with_most_losses_str} have the most losses with a total of {max_losses}.",
            'answer': pitchers_with_most_losses
        })
    else:
        pitcher_with_most_losses = pitchers_with_most_losses[0]
        pairs.append({
            'question': "Who has the most losses?",
            'context': f"{pitcher_with_most_losses} has the most losses with a total of {max_losses}.",
            'answer': pitcher_with_most_losses
        })
    
    # Find the pitcher(s) with the most saves
    max_saves = pitching_data['SV'].max()
    pitchers_with_most_saves = pitching_data.loc[pitching_data['SV'] == max_saves, 'Name'].tolist()
    
    if len(pitchers_with_most_saves) > 1:
        pitchers_with_most_saves_str = ', '.join(pitchers_with_most_saves[:-1]) + ', and ' + pitchers_with_most_saves[-1]
        pairs.append({
            'question': "Who has the most saves?",
            'context': f"{pitchers_with_most_saves_str} have the most saves with a total of {max_saves}.",
            'answer': pitchers_with_most_saves
        })
    else:
        pitcher_with_most_saves = pitchers_with_most_saves[0]
        pairs.append({
            'question': "Who has the most saves?",
            'context': f"{pitcher_with_most_saves} has the most saves with a total of {max_saves}.",
            'answer': pitcher_with_most_saves
        })
    # Find the pitcher(s) with the most innings pitched
    max_ip = pitching_data['IP'].max()
    pitchers_with_most_ip = pitching_data.loc[pitching_data['IP'] == max_ip, 'Name'].tolist()
    
    if len(pitchers_with_most_ip) > 1:
        pitchers_with_most_ip_str = ', '.join(pitchers_with_most_ip[:-1]) + ', and ' + pitchers_with_most_ip[-1]
        pairs.append({
            'question': "Who has pitched the most innings?",
            'context': f"{pitchers_with_most_ip_str} have pitched the most innings with a total of {max_ip}.",
            'answer': pitchers_with_most_ip
        })
    else:
        pitcher_with_most_ip = pitchers_with_most_ip[0]
        pairs.append({
            'question': "Who has pitched the most innings?",
            'context': f"{pitcher_with_most_ip} has pitched the most innings with a total of {max_ip}.",
            'answer': pitcher_with_most_ip
        })
    # Find the pitcher(s) with the most wins
    max_wins = pitching_data['W'].max()
    pitchers_with_most_wins = pitching_data.loc[pitching_data['W'] == max_wins, 'Name'].tolist()
    
    if len(pitchers_with_most_wins) > 1:
        pitchers_with_most_wins_str = ', '.join(pitchers_with_most_wins[:-1]) + ', and ' + pitchers_with_most_wins[-1]
        pairs.append({
            'question': "Who has the most wins?",
            'context': f"{pitchers_with_most_wins_str} have the most wins with a total of {max_wins}.",
            'answer': pitchers_with_most_wins
        })
    else:
        pitcher_with_most_wins = pitchers_with_most_wins[0]
        pairs.append({
            'question': "Who has the most wins?",
            'context': f"{pitcher_with_most_wins} has the most wins with a total of {max_wins}.",
            'answer': pitcher_with_most_wins
        })
    # Find the pitcher(s) with the most hits
    max_hits = pitching_data['H'].max()
    pitchers_with_most_hits = pitching_data.loc[pitching_data['H'] == max_hits, 'Name'].tolist()
    
    if len(pitchers_with_most_hits) > 1:
        pitchers_with_most_hits_str = ', '.join(pitchers_with_most_hits[:-1]) + ', and ' + pitchers_with_most_hits[-1]
        pairs.append({
            'question': "Who has allowed the most hits?",
            'context': f"{pitchers_with_most_hits_str} have allowed the most hits with a total of {max_hits}.",
            'answer': pitchers_with_most_hits
        })
    else:
        pitcher_with_most_hits = pitchers_with_most_hits[0]
        pairs.append({
            'question': "Who has allowed the most hits?",
            'context': f"{pitcher_with_most_hits} has allowed the most hits with a total of {max_hits}.",
            'answer': pitcher_with_most_hits
        })
    # Find the pitcher(s) with the most runs
    max_runs = pitching_data['R'].max()
    pitchers_with_most_runs = pitching_data.loc[pitching_data['R'] == max_runs, 'Name'].tolist()
    
    if len(pitchers_with_most_runs) > 1:
        pitchers_with_most_runs_str = ', '.join(pitchers_with_most_runs[:-1]) + ', and ' + pitchers_with_most_runs[-1]
        pairs.append({
            'question': "Who has allowed the most runs?",
            'context': f"{pitchers_with_most_runs_str} have allowed the most runs with a total of {max_runs}.",
            'answer': pitchers_with_most_runs
        })
    else:
        pitcher_with_most_runs = pitchers_with_most_runs[0]
        pairs.append({
            'question': "Who has allowed the most runs?",
            'context': f"{pitcher_with_most_runs} has allowed the most runs with a total of {max_runs}.",
            'answer': pitcher_with_most_runs
        })
    # Find the pitcher(s) with the highest strikeouts per 9 innings
    max_so9 = pitching_data['SO9'].max()
    pitchers_with_highest_so9 = pitching_data.loc[pitching_data['SO9'] == max_so9, 'Name'].tolist()
    
    if len(pitchers_with_highest_so9) > 1:
        pitchers_with_highest_so9_str = ', '.join(pitchers_with_highest_so9[:-1]) + ', and ' + pitchers_with_highest_so9[-1]
        pairs.append({
            'question': "Who has the highest strikeouts per 9 innings?",
            'context': f"{pitchers_with_highest_so9_str} have the highest strikeouts per 9 innings with a rate of {max_so9}.",
            'answer': pitchers_with_highest_so9
        })
    else:
        pitcher_with_highest_so9 = pitchers_with_highest_so9[0]
        pairs.append({
            'question': "Who has the highest strikeouts per 9 innings?",
            'context': f"{pitcher_with_highest_so9} has the highest strikeouts per 9 innings with a rate of {max_so9}.",
            'answer': pitcher_with_highest_so9
        })
    # Filter out pitchers with less than 25 innings pitched
    filtered_pitching_data = pitching_data[pitching_data['IP'] >= 25]
    
    # Find the pitcher(s) with the highest strikeouts per 9 innings
    max_so9 = filtered_pitching_data['SO9'].max()
    pitchers_with_highest_so9 = filtered_pitching_data.loc[filtered_pitching_data['SO9'] == max_so9, 'Name'].tolist()
    
    if len(pitchers_with_highest_so9) > 1:
        pitchers_with_highest_so9_str = ', '.join(pitchers_with_highest_so9[:-1]) + ', and ' + pitchers_with_highest_so9[-1]
        pairs.append({
            'question': "Who has the highest strikeouts per 9 innings (minimum 25 innings pitched)?",
            'context': f"{pitchers_with_highest_so9_str} have the highest strikeouts per 9 innings with a rate of {max_so9} (minimum 25 innings pitched).",
            'answer': pitchers_with_highest_so9
        })
    else:
        pitcher_with_highest_so9 = pitchers_with_highest_so9[0]
        pairs.append({
            'question': "Who has the highest strikeouts per 9 innings (minimum 25 innings pitched)?",
            'context': f"{pitcher_with_highest_so9} has the highest strikeouts per 9 innings with a rate of {max_so9} (minimum 25 innings pitched).",
            'answer': pitcher_with_highest_so9
        })
    # Filter out pitchers with less than 10 innings pitched
    filtered_pitching_data = pitching_data[pitching_data['IP'] >= 10]
    
    # Find the pitcher(s) with the lowest batting average on balls in play
    min_babip = filtered_pitching_data['BAbip'].min()
    pitchers_with_lowest_babip = filtered_pitching_data.loc[filtered_pitching_data['BAbip'] == min_babip, 'Name'].tolist()
    
    if len(pitchers_with_lowest_babip) > 1:
        pitchers_with_lowest_babip_str = ', '.join(pitchers_with_lowest_babip[:-1]) + ', and ' + pitchers_with_lowest_babip[-1]
        pairs.append({
            'question': "Who has the lowest batting average on balls in play (minimum 10 innings pitched)?",
            'context': f"{pitchers_with_lowest_babip_str} have the lowest batting average on balls in play with a rate of {min_babip} (minimum 10 innings pitched).",
            'answer': pitchers_with_lowest_babip
        })
    else:
        pitcher_with_lowest_babip = pitchers_with_lowest_babip[0]
        pairs.append({
            'question': "Who has the lowest batting average on balls in play (minimum 10 innings pitched)?",
            'context': f"{pitcher_with_lowest_babip} has the lowest batting average on balls in play with a rate of {min_babip} (minimum 10 innings pitched).",
            'answer': pitcher_with_lowest_babip
        })
    # Find the pitcher(s) with the most games started
    max_gs = pitching_data['GS'].max()
    pitchers_with_most_gs = pitching_data.loc[pitching_data['GS'] == max_gs, 'Name'].tolist()
    
    if len(pitchers_with_most_gs) > 1:
        pitchers_with_most_gs_str = ', '.join(pitchers_with_most_gs[:-1]) + ', and ' + pitchers_with_most_gs[-1]
        pairs.append({
            'question': "Who has the most games started?",
            'context': f"{pitchers_with_most_gs_str} have the most games started with a total of {max_gs}.",
            'answer': pitchers_with_most_gs
        })
    else:
        pitcher_with_most_gs = pitchers_with_most_gs[0]
        pairs.append({
            'question': "Who has the most games started?",
            'context': f"{pitcher_with_most_gs} has the most games started with a total of {max_gs}.",
            'answer': pitcher_with_most_gs
        })
    # Sort the pitching data by games started (GS) in descending order
    sorted_pitching_data = pitching_data.sort_values('GS', ascending=False)
    
    # Get the top 10 pitchers with the most games started
    top_10_pitchers_gs = sorted_pitching_data.head(10)['Name'].tolist()
    
    # Append the question, context, and answer to the `pairs` list
    pairs.append({
        'question': "Who are the top 10 pitchers with the most games started?",
        'context': f"The top 10 pitchers with the most games started are: {', '.join(top_10_pitchers_gs)}.",
        'answer': top_10_pitchers_gs
    })
    # Count the number of pitchers who have started a game this year
    pitchers_with_gs = pitching_data[pitching_data['GS'] >= 1]['Name'].nunique()
    
    # Append the question, context, and answer to the `pairs` list
    pairs.append({
        'question': "How many pitchers have started a game this year?",
        'context': f"A total of {pitchers_with_gs} pitchers have started a game this year.",
        'answer': pitchers_with_gs
    })
    
    # Count the number of pitchers who have recorded a save this year
    pitchers_with_sv = pitching_data[pitching_data['SV'] >= 1]['Name'].nunique()
    
    # Append the question, context, and answer to the `pairs` list
    pairs.append({
        'question': "How many pitchers have recorded a save this year?",
        'context': f"A total of {pitchers_with_sv} pitchers have recorded a save this year.",
        'answer': pitchers_with_sv
    })
    
    # Find the pitcher(s) with the best (lowest) WHIP
    min_whip = pitching_data['WHIP'].min()
    pitchers_with_best_whip = pitching_data.loc[pitching_data['WHIP'] == min_whip, 'Name'].tolist()
    
    if len(pitchers_with_best_whip) > 1:
        pitchers_with_best_whip_str = ', '.join(pitchers_with_best_whip[:-1]) + ', and ' + pitchers_with_best_whip[-1]
        pairs.append({
            'question': "Who has the best (lowest) WHIP?",
            'context': f"{pitchers_with_best_whip_str} have the best (lowest) WHIP with a value of {min_whip}.",
            'answer': pitchers_with_best_whip
        })
    else:
        pitcher_with_best_whip = pitchers_with_best_whip[0]
        pairs.append({
            'question': "Who has the best (lowest) WHIP?",
            'context': f"{pitcher_with_best_whip} has the best (lowest) WHIP with a value of {min_whip}.",
            'answer': pitcher_with_best_whip
        })
    # Filter out pitchers with less than 20 innings pitched
    filtered_pitching_data = pitching_data[pitching_data['IP'] >= 20]
    
    # Sort the filtered pitching data by WHIP in ascending order
    sorted_pitching_data = filtered_pitching_data.sort_values('WHIP', ascending=True)
    
    # Get the top 5 pitchers with the best WHIP
    top_5_pitchers_whip = sorted_pitching_data.head(5)
    
    # Append the question, context, and answer to the `pairs` list
    pairs.append({
        'question': "Who are the pitchers with the 5 best WHIP (minimum 20 innings pitched)?",
        'context': f"The pitchers with the 5 best WHIP (minimum 20 innings pitched) are:",
        'answer': top_5_pitchers_whip[['Name', 'WHIP']].to_dict(orient='records')
    })
    # Filter the pitching data for Lance Lynn
    lance_lynn_data = pitching_data[pitching_data['Name'] == 'Lance Lynn']
    
    # Get the total number of strikeouts for Lance Lynn
    total_strikeouts = lance_lynn_data['SO'].sum()
    
    # Append the question, context, and answer to the `pairs` list
    pairs.append({
        'question': "How many strikeouts does Lance Lynn have?",
        'context': f"Lance Lynn has {total_strikeouts} strikeouts.",
        'answer': total_strikeouts
    })
    
    # Loop through each unique pitcher in the data
    for pitcher in pitching_data['Name'].unique():
        # Filter the pitching data for the current pitcher
        pitcher_data = pitching_data[pitching_data['Name'] == pitcher]

        # Get the total number of strikeouts for the current pitcher
        total_strikeouts = pitcher_data['SO'].sum()

        # Generate the question and answer for the current pitcher
        question = f"How many strikeouts does {pitcher} have?"
        context = f"{pitcher} has {total_strikeouts} strikeouts."
        answer = total_strikeouts

        # Append the question-answer pair to the list
        pairs.append({
            'question': question,
            'context': context,
            'answer': answer
        })
        

    return pairs

# Generate question-answer pairs for the batting stats DataFrame
batting_pairs = generate_qa_pairs_batting()
pitching_pairs = generate_qa_pairs_pitching('data/pitching_stats.csv')
qa_pairs = batting_pairs + pitching_pairs

# Save the question-answer pairs to a CSV file
qa_df = pd.DataFrame(qa_pairs)
qa_df.to_csv('train/qa_dataset.csv', sep='\t', index=False)

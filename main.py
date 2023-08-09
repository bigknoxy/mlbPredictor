import statsapi

# Get the standings for the American League East division
standings = statsapi.standings(leagueId=103, divisionId=201)
thing = statsapi

# Print the standings
print(standings)


# # Get the runs scored by each team.
# runs_scored = {}
# runs_scored[game.away_team.name] = game.away_team.runs_scored
# runs_scored[game.home_team.name] = game.home_team.runs_scored

# # Get the ERA of each team's starting pitcher.
# era = {}
# era[game.away_team.name] = game.away_team.starting_pitcher.era
# era[game.home_team.name] = game.home_team.starting_pitcher.era

# # Get the strikeout rate of each team's starting pitcher.
# strikeout_rate = {}
# strikeout_rate[game.away_team.name] = game.away_team.starting_pitcher.strikeout_rate
# strikeout_rate[game.home_team.name] = game.home_team.starting_pitcher.strikeout_rate

# # Print the results.
# print("Team | Runs Scored | ERA | Strikeout Rate")
# print(game.away_team.name, runs_scored[game.away_team.name], era[game.away_team.name], strikeout_rate[game.away_team.name])
# print(game.home_team.name, runs_scored[game.home_team.name], era[game.home_team.name], strikeout_rate[game.home_team.name])


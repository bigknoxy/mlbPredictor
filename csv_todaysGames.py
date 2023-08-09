import pandas as pd
from pandasai import PandasAI
import statsapi as mlb
import datetime


#get today's date
today = datetime.date.today()
today_string = today.strftime('%m/%d/%Y')
#get today's schedule
sched = mlb.schedule(today_string)
sched_df = pd.DataFrame(sched)

#output to CSV file
sched_df.to_csv('data/todaysGames.csv', index=False)


from pybaseball import batting_stats_bref, statcast_batter_expected_stats

# Get all of this season's batting data so far
batting_stats = batting_stats_bref()

# Get data for batters with a minimum of 50 plate appearances in 2023
expected_batting_stats = statcast_batter_expected_stats(2023, 50)

# Write the data to a CSV file
batting_stats.to_csv('data/batting_stats.csv', index=False)
expected_batting_stats.to_csv('data/expected_batting_stats.csv', index=False)

from pybaseball import statcast_pitcher_expected_stats, pitching_stats_bref

#get all of this seasons pitching data
pitching_stats = pitching_stats_bref()

#get expected pitching stats
expected_pitching_stats = statcast_pitcher_expected_stats(2023, 50)

#output data to csv file in data folder
pitching_stats.to_csv('data/pitching_stats.csv', index=False)
expected_pitching_stats.to_csv('data/expected_pitching_stats.csv', index=False)

#imports
import pandas as pd
import numpy as np
import statsapi as mlb
from transformers import AutoModelForSequenceClassification
from pybaseball import statcast
from pybaseball import pitching_stats_bref
from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
import datetime


#get today's date
today = datetime.date.today()

#get today's schedule
sched = mlb.schedule(today.strftime('%m/%d/%Y'))
print('--------SCHEDULE-----------------------------------------------------')
print(sched)

# get pitching stats for this year
pitching_current_year_stats = pitching_stats_bref()
print('--------PITCHER CURRENT YEAR STATS-----------------------------------------------------')
print(pitching_current_year_stats)

# Get list of today's starting pitcher
today_starting_pitchers = []
for game in sched:
  if game['status'] in ('Pre-Game', 'Scheduled'):
      home_pitcher = game['home_probable_pitcher']
      away_pitcher = game['away_probable_pitcher']
      if home_pitcher:
        today_starting_pitchers.append(home_pitcher)
      if away_pitcher:
        today_starting_pitchers.append(away_pitcher)

print('-----------TODAY STARTING PITCHERS--------------------------------------------------')
print(today_starting_pitchers)


# from pybaseball import player_search_list

# # Create a list of last names and first names
# names = []
# for pitcher in today_starting_pitchers:
#     pitcher_name = pitcher.split()
#     names.append((pitcher_name[1], pitcher_name[0]))

# # Get the data for today's starting pitchers
# todays_starting_pitchers_with_ids = player_search_list(names)

# print(todays_starting_pitchers_with_ids)

# # Convert the key_mlbam column to an int array
# key_mlbam_int_array = todays_starting_pitchers_with_ids['key_mlbam'].astype(int)

# # Print the key_mlbam_int_array
# print(key_mlbam_int_array)

print('-------------------------------------------------------------')
# Get the pitching data for today's starting pitchers only
# todays_starting_pitchers_stats = pd.DataFrame()
# for pitcher in today_starting_pitchers:
#     record = pitching_current_year_stats.loc[pitching_current_year_stats['Name'] == pitcher]
#     todays_starting_pitchers_stats = todays_starting_pitchers_stats.append(record, ignore_index=True)

# print(todays_starting_pitchers_stats)


print('--------EXPECTED PITCHER STATS-----------------------------------------------------')
from pybaseball import statcast_pitcher_expected_stats

# get data for all qualified pitchers in current year
expected_pitching_stats = statcast_pitcher_expected_stats(today.year)
print(expected_pitching_stats)


print('--------BATTER STATS current year-----------------------------------------------------')
from pybaseball import batting_stats_bref

# get all of this season's batting data so far
batting_stats = batting_stats_bref()
print(batting_stats)

print('--------EXPECTED BATTER STATS min 50 At Bats-----------------------------------------------------')

from pybaseball import statcast_batter_expected_stats

# get data for batters with a minimum of 50 plate appearances in 2023
expected_batting_stats = statcast_batter_expected_stats(2023, 50)
print(expected_batting_stats)
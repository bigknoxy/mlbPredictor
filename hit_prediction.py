from pybaseball import statcast_batter_expected_stats

# get data for batters with a minimum of 150 plate appearances in 2019
data = statcast_batter_expected_stats(2019, 150)
print(data)
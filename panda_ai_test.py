# 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

import pandas as pd
import pandasai as PandasAI

# other imports
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

batter_stats = mlb
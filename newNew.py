import pybaseball
# test pandas ai
import pandas as pd
from pandasai import PandasAI
import statsapi as mlb
import datetime

from pybaseball import batting_stats_bref
# get all of this season's batting data so far
data = batting_stats_bref()
data_df = pd.DataFrame(data)

from pandasai.llm.starcoder import Starcoder
# Starcoder
llm = Starcoder(api_token="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")
pandas_ai = PandasAI(llm)
pandas_ai(data_df,'Who are home run leaders? ')
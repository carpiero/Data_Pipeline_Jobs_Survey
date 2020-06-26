import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from functools import reduce

# acquisition functions

def get_tables(path):
    engine = create_engine(f'sqlite:///{path}')
    df_personal = pd.read_sql("SELECT * FROM personal_info" , engine)
    df_country = pd.read_sql("SELECT * FROM country_info" , engine)
    df_career = pd.read_sql("SELECT * FROM career_info" , engine)
    df_poll = pd.read_sql("SELECT * FROM poll_info" , engine)
    dfs = [df_personal , df_country , df_career , df_poll]
    df_final = reduce(lambda left , right: pd.merge(left , right , on='uuid') , dfs)
    return df_final

def clean(dataframe):
    dataframe_clean = dataframe

    return dataframe_clean




def acquire():
    return clean(get_tables('./data/raw/raw_data_project_m1.db'))


















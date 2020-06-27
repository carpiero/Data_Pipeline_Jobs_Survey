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

def clean(df_clean):
    ''' cleaning age column '''

    df_clean['age'] = df_clean['age'].str.replace(' years old' , '')
    for x in range(1980 , 2087):
        df_clean['age'] = df_clean['age'].str.replace(f'{x}' , f'{2016 - x}')
    df_clean['age'] = df_clean['age'].astype('int64')


    ''' cleaning gender column '''

    df_clean['gender'] = df_clean['gender'].str.replace(r'\bmale\b' , 'Male') \
                                            .str.replace(r'\bFem\b' , 'Female') \
                                            .str.replace(r'\bFeMale\b' , 'Female') \
                                            .str.replace(r'\bfemale\b' , 'Female')
    df_clean['gender'] = df_clean['gender'].astype('category')


    ''' cleaning dem_has_children column '''

    df_clean['dem_has_children'] = df_clean['dem_has_children'].str.replace(r'\bNO\b' , 'no') \
                                                                .str.replace(r'\byES\b' , 'yes') \
                                                                .str.replace(r'\bnO\b' , 'no') \
                                                                .str.replace(r'\bYES\b' , 'yes')
    df_clean['dem_has_children'] = df_clean['dem_has_children'].astype('category')


    ''' cleaning age_group column '''

    df_clean['age_group'] = df_clean['age_group'].str.replace(r'\bjuvenile\b' , '14_25')
    df_clean['age_group'] = df_clean['age_group'].astype('category')


    ''' cleaning country_code column '''

    df_clean['country_code'] = df_clean['country_code'].str.replace(r'\bGB\b' , 'UK') \
                                                        .str.replace(r'\bGR\b' , 'EL')
    df_clean['country_code'] = df_clean['country_code'].astype('category')






    return df_clean




def acquire(path):
    return clean(get_tables(path))


















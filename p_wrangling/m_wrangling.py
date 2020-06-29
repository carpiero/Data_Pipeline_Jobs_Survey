
# wrangling functions

def fillnulls(df_fillnulls):

    df_fillnulls.loc[df_fillnulls['Job Title'].isnull() , 'Job Title'] = 'Unemployed or Part time Job or Inactive'

    return df_fillnulls


def wrangle(data):

    return fillnulls(data)
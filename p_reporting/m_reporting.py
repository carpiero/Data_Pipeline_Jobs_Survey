

# reporting functions

def specific_country(df_specific_country, country):

#    df_specific_country = df_specific_country.loc[df_specific_country['Country']\
#        .str.contains(country)].sort_values(by='Quantity' , ascending=False)

    return df_specific_country






def reporting(results,country):


    print(specific_country(results,country).info(memory_usage='deep'))
    print(specific_country(results,country).nunique())
    print(specific_country(results,country))
    print('========================= Pipeline is complete. You may find the results in the folder ./data/results =========================')


    return specific_country(results,country)
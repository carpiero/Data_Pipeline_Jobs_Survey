import re
import pandas as pd

# reporting functions

def specific_country(results,country):

    country_list = results['Country'].unique().tolist()
    pd.DataFrame(results['Country'].unique()).to_csv('./data/results/country_list.csv')

    if country == None:
        print('\n\n============================ Below you could see the table of content with all the countries  ====================================\n\n')
        return results

    elif not isinstance(country , str):
        return '\n=================================================================================================\n\nError, please insert a correct Country of the list inside ./data/results/country_list.csv\n\n'

    elif country not in country_list:
        country = country.lower()
        country = country.title()
        if country not in country_list:
            return '\n=================================================================================================\n\nError, please insert a correct Country of the list inside ./data/results/country_list.csv\n\n'
        else:
            print(f'\n\n============================ Below you could see the table of content of {country}   ====================================\n\n')
            df_specific_country = results.loc[results['Country'] \
                .str.contains(country)].sort_values(by='Quantity' , ascending=False)
            return df_specific_country


    else:
        print(f'\n\n============================ Below you could see the table of content of {country}   ====================================\n\n')
        df_specific_country = results.loc[results['Country'] \
            .str.contains(country)].sort_values(by='Quantity' , ascending=False)
        return df_specific_country


def reporting(results,country):
    # country_list = results['Country'].unique().tolist()
    #
    # if country == None:
    #     print('\n\n============================ Below you could see the table of content with all the countries  ====================================\n\n')
    #     return results
    #
    # elif country not in country_list:
    #     return
    #
    #
    # else:
    #     print(f'\n\n============================ Below you could see the table of content of {country}   ====================================\n\n')
    #     df_specific_country = results.loc[results['Country'] \
    #     .str.contains(country)].sort_values(by='Quantity' , ascending=False)
        return specific_country(results,country)


    # print(specific_country(results,country).info(memory_usage='deep'))
    # print(specific_country(results,country).nunique())
    # print(specific_country(results,country))


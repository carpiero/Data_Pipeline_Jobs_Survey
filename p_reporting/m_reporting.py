import re
import pandas as pd

# reporting functions

def specific_country(results,country):

    country_list = results['Country'].unique().tolist()
    pd.DataFrame(results['Country'].unique()).to_csv('./data/results/country_list.csv')

    if not isinstance(country , str):
        print('Error, please insert a correct Country of the list inside ./data/results/country_list.csv')
        print('============================ Below you could see the table of content with all the countries  ====================================')
    else:
        if country not in country_list:
            country = country.lower()
            country = country.title()
            country = re.sub(r' ' , '' , country)
            if country not in country_list:
                print('Error, please insert a correct Country of the list inside ./data/results/country_list.csv')
                print('============================ Below you could see the table of content with all the countries  ====================================')

            else:
                return country

        else:
            return country



def reporting(results,country):

    if country == None:
        print('============================ Below you could see the table of content with all the countries  ====================================')
        return results
    else:
        df_specific_country = results.loc[results['Country'] \
        .str.contains(country)].sort_values(by='Quantity' , ascending=False)
        return df_specific_country


    # print(specific_country(results,country).info(memory_usage='deep'))
    # print(specific_country(results,country).nunique())
    # print(specific_country(results,country))


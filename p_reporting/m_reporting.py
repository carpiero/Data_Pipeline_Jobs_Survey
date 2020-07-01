import pandas as pd

# reporting functions

def specific_country(results,country):

    country_list = results['Country'].unique().tolist()
    pd.DataFrame(results['Country'].unique()).to_csv('./data/results/country_list.csv')

    if country == None:

        print('\n\n============================ Below you could see the table of content with all the countries  ====================================\n\n')

        return results

    else:
        if country not in country_list:
            country = country.lower()
            country = country.title()

            if country not in country_list:
                raise NameError


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

        return specific_country(results,country)


# if country == None:
    #     print('\n\n============================ Below you could see the table of content with all the countries  ====================================\n\n')
    #
    #     return results
    #
    # elif country not in country_list:
    #     country = country.lower()
    #     country = country.title()
    #     if country not in country_list:
    #
    #         return '\n=================================================================================================\n\nError, please insert a correct Country of the list inside ./data/results/country_list.csv\n\n=================================================================================================\n\n'
    #
    #     else:
    #         print(f'\n\n============================ Below you could see the table of content of {country}   ====================================\n\n')
    #
    #         df_specific_country = results.loc[results['Country'] \
    #             .str.contains(country)].sort_values(by='Quantity' , ascending=False)
    #
    #         return df_specific_country
    #
    #
    # else:
    #     print(f'\n\n============================ Below you could see the table of content of {country}   ====================================\n\n')
    #
    #     df_specific_country = results.loc[results['Country'] \
    #         .str.contains(country)].sort_values(by='Quantity' , ascending=False)
    #
    #     return df_specific_country
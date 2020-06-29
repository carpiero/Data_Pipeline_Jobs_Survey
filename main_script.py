
import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set country')
    parser.add_argument("-c", "--country", help="specify country for the results", type=str)#, required=True)
    parser.add_argument("-p" , "--path" , help="specify the path of the database, the file .db" , type=str,required=True)
    args = parser.parse_args()
    return args

def main(arguments):

    data = mac.acquire(arguments.path)
    filtered = mwr.wrangle(data)
    results = man.analyze(filtered)
    results.to_csv('./data/results/df_results.csv')

    #reporting = mre.reporting(results, arguments.country)
    print(reporting)


 #   print('========================= Pipeline is complete. You may find the results in the folder ./data/results =========================')

if __name__ == '__main__':
#    year = int(input('Enter the year: '))
#    title = 'Top 10 Manufacturers by Fuel Efficiency ' + str(year)
    arguments = argument_parser()
    main(arguments)
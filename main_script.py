import argparse
from p_acquisition import m_acquisition as mac
#from p_wrangling import m_wrangling as mwr
#from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set country')
    parser.add_argument("-c", "--country", help="specify country for the results", type=str)
    args = parser.parse_args()
    return args

def main(arguments):
    print(mac.acquire())
    print(mac.acquire().info(memory_usage='deep'))
    print(mac.acquire().nunique())
#    data = mac.acquire(arguments.path)
#    filtered = mwr.wrangle(data, year)
 #   results = man.analyze(filtered)
 #   fig = mre.plotting_function(results, title, arguments)
 #   mre.save_viz(fig, title)
    print('========================= Pipeline is complete. You may find the results in the folder ./data/results =========================')

if __name__ == '__main__':
#    year = int(input('Enter the year: '))
#    title = 'Top 10 Manufacturers by Fuel Efficiency ' + str(year)
    arguments = argument_parser()
    main(arguments)
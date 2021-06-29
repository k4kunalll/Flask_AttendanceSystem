import pandas as pd
import os


def create_database(database_name):

    if os.path.exists('{}.pkl'.format(database_name)) == False:
        df = pd.DataFrame()
        df.to_pickle('{}.pkl'.format(database_name))
        print('---Database Created Successfully---')
    
    else:
        print('Database Exists')


# create_database('database')
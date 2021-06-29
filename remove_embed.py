import pandas as pd
import shutil

def remove_class(database, class_id):

    df = pd.read_pickle('{}.pkl'.format(database))

    class_name = class_id

    extract_class = df[df['Class'] == class_name]
    class_index = extract_class.index

    new_df = df.drop(class_index, axis = 0)

    new_df.reset_index(inplace=True, drop=True)

    new_df.to_pickle('{}.pkl'.format(database))

    print('{} class removed Successfully from Database'.format(class_name))


def remove_folder(folder_path):

    shutil.rmtree(folder_path)

    print('--Folder Deleted Successfully')


# remove_class('database', 'kunal')

# remove_folder('test/shahrukh')
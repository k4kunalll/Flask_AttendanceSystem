import numpy as np 
import pandas as pd
import os
import face_recognition


def newuser(database, username):

    image_data = []
    embeddings = []
    index = []

    data_path = 'data'
    folder_name = username

    user_folder = os.listdir(os.path.join(data_path, folder_name))

    #extracting all class folders
    for images in user_folder:
        image_data.append(os.path.join(data_path, folder_name) + '/' +  images)

    #embedding function
    def create_embedding(path):

        img = face_recognition.load_image_file(path)
        try:
            img = face_recognition.face_encodings(img)[0]
            return img

        except:
            img = 'No Embeddings'
            return img

    for i in range(len(image_data)):

        print('Converting Image {} to Embeddings'.format(image_data[i]))
        image_names = image_data[i]
        # index.append(folder_name)
        z = create_embedding(image_names)

        if type(z) == type(np.array(5)):
            embeddings.append(z)
            index.append(folder_name)           
        else:
            pass

    # dictionary of lists 
    dict = {'Embeddings': embeddings, 'Class': index} 

    df = pd.read_pickle('{}.pkl'.format(database))

    df2 = pd.DataFrame(dict)

    df_new = pd.concat([df, df2], ignore_index=True)

    # saving the dataframe
    # df.to_csv('embedding.csv', header=True, index=False)
    df_new.to_pickle('{}.pkl'.format(database))

    print(' ---- Embeddings created Successfully !!! ---- \n---- Saved Successfully in Databas ----')
    print('---- {} total entries in Database ----'.format(len(df_new)))

# database = 'database'
# username = 'goku'
# newuser(database, username) 
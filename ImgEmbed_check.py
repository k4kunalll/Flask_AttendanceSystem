
from face_recognition.api import face_distance
import numpy as np 
import pandas as pd
import face_recognition
from collections import Counter

def img_embedding(path):

    img = face_recognition.load_image_file(path)
    try:
        img = face_recognition.face_encodings(img)[0]
        return img

    except:
        img = 'No Embeddings'
        return img


def check_img(encoded_image, database):

    face_check = []

    same_match = 0
    different_match = 0

    df = pd.read_pickle('{}.pkl'.format(database))
    for i in range(len(df['Embeddings'])):
        saved_embed = df['Embeddings'][i]
        zz = face_recognition.compare_faces([encoded_image], saved_embed, tolerance=0.5)
        # distance = face_distance([encoded_image], saved_embed)    
        class_match = df['Class'][i]
        
        if zz[0] == True:
            same_match = same_match+1
            fl = True
            face_match = class_match.upper()
            face_check.append(face_match)
            # print('Face Matches With {}'.format(class_match))
            # print('Distance', distance)
        elif zz[0] == False:
            different_match = different_match+1
            # print('Distance', distance)

        # print('Class Compared', df['Class'][i])
    print('{} same matches found'.format(same_match))
    # print('{} different maches found'.format(different_match))

  
    counting_occurrence = Counter(face_check)
    max_occurrence = counting_occurrence.most_common(1)[0][0]
    print(max_occurrence)

    if same_match == 0:
        print('--New Class Found--')
    else:
        print('--No new Class Found--')

    if fl == True:
        return max_occurrence

    else:
        return 'NO MATCHES FOUND'

    


# img_path = 'data/kunal/kunal303.jpg'
# database = 'database'
# img_encode = img_embedding(img_path)
# check_img(img_encode, database)
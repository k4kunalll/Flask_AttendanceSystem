import pandas as pd
import time  
from csv import writer
import os


def attendance(username):

    import time                    
    attendance = username
    date = time.asctime(time.gmtime())[3 : -14]
    time = time.asctime(time.gmtime())[10 : -5]

    if os.path.exists('AttendanceLogs.csv') == False:
        df = pd.DataFrame()
        # saving the dataframe
        df.to_csv('AttendanceLogs.csv')
        print('dataframe created')
    
    # List 
    List = [attendance, date, time]
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('AttendanceLogs.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
    
        #Close the file object
        f_object.close()

    return 'Attendance Marked'


# attendance('yyuu')


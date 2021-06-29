from flask import Flask, render_template, Response, request, redirect 
import cv2
from imutils.video import VideoStream
import imutils
import random
import os
from ImgEmbed_check import *
from newuser_add import *
from attendance_file import *
from remove_embed import *
from createdb import *

app = Flask(__name__)
# videoStream = cv2.VideoCapture('0')
videoStream = VideoStream(src=0).start()
# time.sleep(20.0)

glob_username = str()

def generateFrames():
    while True:
        frame = videoStream.read()
        frame = imutils.resize(frame)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template('homepage.html')


@app.route("/liveCam", methods = ['GET', 'POST'])
def video():
    return Response(generateFrames(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


@app.route('/markAttendance', methods = ['GET', 'post'])
def markattendance():  
    while True:
        frame = videoStream.read()
        # frame = imutils.resize(frame)
        frame = cv2.resize(frame, (400, 300))
        cv2.imwrite('attendance/1.jpg', frame)

        try:
            img_path = 'attendance/1.jpg'
            img_encode = img_embedding(img_path)
            c = check_img(img_encode, 'database')
            d = '{} Attendance Marked'.format(c)
            attendance(c)
        except:
            d = 'Class not found'

        return render_template('homepage.html', output = d)      
    


@app.route("/registration", methods = ['GET', 'POST'])
def registeruser():
    return render_template('register.html')


@app.route('/confirmUserName', methods = ['GET', 'post'])
def username():  
    
    global glob_username

    if request.method == 'POST':

        req = request.form
        
        user_name = req["username"]

        glob_username = user_name

        os.mkdir('data/{}'.format(user_name))

        return redirect(request.url)

    
    return render_template('register.html')     



@app.route('/captureUser', methods = ['GET', 'post'])
def imageCapture():  

    global glob_username

    while True:
        frame = videoStream.read()
        # frame = imutils.resize(frame)
        frame = cv2.resize(frame, (400, 300))
        cv2.imwrite('data/{one}/{one}{two}.jpg'.format(one = glob_username, two = random.randint(0, 500)), frame)

        return render_template('register.html')      

@app.route('/addUserEntry', methods = ['GET', 'post'])
def adduser():  

    global glob_username

    database = 'database'
    create_database(database)
    username = glob_username
    newuser(database, username) 

    return render_template('register.html')      


@app.route("/removeUser", methods = ['GET', 'POST'])
def removeruser():
    return render_template('remove.html')


@app.route('/confirmRemoveUser', methods = ['GET', 'post'])
def user_remove_name():  
    
    global glob_username

    if request.method == 'POST':
        req = request.form       
        user_name = req["username"]
        glob_username = user_name

        return redirect(request.url)
    return render_template('remove.html')  


@app.route('/removeUserEntry', methods = ['GET', 'post'])
def removeuserdata():  

    global glob_username

    database = 'database'
    class_name = glob_username
    folder_path = 'data' + '/' + class_name
    remove_class(database, class_name)
    remove_folder(folder_path)

    return render_template('remove.html') 


if __name__ == '__main__':
    app.run()
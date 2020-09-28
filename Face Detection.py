import pyttsx3 as r
engine = r.init()
import os
import cv2
import numpy as n
import time
import face_recognition
def speak(n):
    engine.say(n)
    engine.runAndWait()
    return
def face():
    #haarcascade is used in order to use face detection
    faceDetect=cv2.CascadeClassifier('E:\python project\Face Detection Program Full\package used for face detection\camera access package for python\opencv Extracted file\sources\data\haarcascades\haarcascade_frontalface_default.xml')#using haarcascade for face detection and given the full path of haarcade 
    cam=cv2.VideoCapture(0)
    p=speak("starting camera to scan you face")
    time.sleep(1)
    i=1
    if i==1:
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            i=1+1
            cv2.imwrite("E:/python project/Face Detection Program Full/Data Base/Temporary Data Base/unknow person.jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
            cv2.waitKey(100)
        cv2.imshow("Face Detection",img)
        cv2.waitKey(100)
        i+=1
    cam.release()
    cv2.destroyAllWindows()
    o="\m"
    f1="/m"
    e=""
    c=0
    permanent_path="E:\python project\Face Detection Program Full\Data Base\Permanent Data Base"
    permanent_file_name=[]
    permanent_file_path=[]
    temporary_path="E:\python project\Face Detection Program Full\Data Base\Temporary Data Base"
    temporary_file_name=[]
    temporary_file_path=[]
    for a in os.listdir(permanent_path):
        permanent_file_name.append(a)
    l=len(permanent_file_name)
    for b in os.listdir(temporary_path):
        temporary_file_name.append(b)
    temp_image=temporary_path+o[0]+temporary_file_name[0]
    unknown=face_recognition.load_image_file(temp_image)
    unknown_encode=face_recognition.face_encodings(unknown)[0]
    for a in permanent_file_name:
        permanent_image=permanent_path+o[0]+a
        known=face_recognition.load_image_file(permanent_image)
        known_encode=face_recognition.face_encodings(known)[0]  
        result=face_recognition.compare_faces([known_encode],unknown_encode)
        if result[0]:
            l=len(a)
            for i in range(0,l-4):
                e+=a[i]
            name=e
            e=""
            for i in range(len(temp_image)):
                if temp_image[i]==o[0]:
                    e+=f1[0]
                else:
                    e+=temp_image[i]
            os.remove(e)
            return name
            break
        else:
            c+=1
    if c==l:
        p=speak("Access Denied")
        for i in range(len(temp_image)):
            if temp_image[i]==o[0]:
                e+=f1[0]
            else:
                e+=temp_image[i]
        os.remove(e)
        name="your not allowed to access this file"
        return name

import numpy as np
import RPi.GPIO as GPIO
import time
import cv2
import sys




w1 = 'w1'
cap = cv2.VideoCapture(0)
 

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')
cond = True
while cond:
    ret, image = cap.read()
    if ret== False:
        break
    temp = image
    gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3 ,5 )
    for(x,y,w,h) in faces:
        '''cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)'''
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            '''cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)'''
            image[y:y+h,x:x+w] = roi_color
        cond = False
    
        
        
cv2.imwrite('face.jpg', temp)

cap.release()

print('Program terminated successfuly')
import mailer

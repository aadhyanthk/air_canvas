import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import keyboard

from datetime import datetime as d
import time as t
from os import system as clear
cls = lambda: clear("clear")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

l = 1280
b = 720
oval = 90

cap.set(3, l)
cap.set(4, b)

#this variable decides weather line should be straight or not
straightLine = True

#this is a list of points ----------------------------------------------------
points = []
pointsmo = [] #todo
#-----------------------------------------------------------------------------

#These values will be used to check the time difference between two points drawn
thisTime = 0
previousTime = 0
#-------------------------------------------------------------------------------

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # remove background of image
        # https://python.plainenglish.io/how-to-remove-image-background-using-python-6f7ffa8eab15
        # Detections
        #print(results)
        
        #print(results.multi_hand_landmarks)
        # Rendering results
        
        #Grid------------------------------------------------------------------
    
        for i in range(oval- int(oval/2), l, oval):
            for j in range(oval- int(oval/2), b, oval):
                cv2.circle(image, (int(i),int(j)), 1, (100, 100, 100), 2)
        #----------------------------------------------------------------------
        
        if results.multi_hand_landmarks:
            
            
            for num, hand in enumerate(results.multi_hand_landmarks):
                #print(hand[0].landmark[0])
                
                x = 640 # default x
                y = 480 # default y
                
                #actual x and y
                x1 = results.multi_hand_landmarks[0].landmark[8].x * l
                y1 = results.multi_hand_landmarks[0].landmark[8].y * b
                
                
                #Add points in the list----------------------------------------
                z1 = results.multi_hand_landmarks[0].landmark[8].z
                
                #print(z1)
                
                if(z1 < -0.03 and straightLine):
                    color = (121, 22, 76)
                    ts = d.now()
                    ts = int(ts.strftime("%S"))
                    tm = d.now()
                    tm = int(tm.strftime("%M"))
                    thisTime = tm * 1000 + ts

                    points.append([x1,y1,thisTime])
                    
                else:
                    if(z1 < -0.03 and not straightLine):
                        color = (121, 22, 76)
                        ts = d.now()
                        ts = int(ts.strftime("%S"))
                        tm = d.now()
                        tm = int(tm.strftime("%M"))
                        thisTime = tm * 1000 + ts

                        pointsmo.append([x1,y1,thisTime])
                    
                    else:
                        if straightLine:
                            color = (0,0,200)
                        else:
                            color = (0,200,200)
                
                #--------------------------------------------------------------
                
                
                
                
                x1 = int(x1) * 1
                y1 = int(y1) * 1
                
                x1 += 0
                y1 += 0
                
                #print(z1)
                #print(results.multi_hand_landmarks[0].landmark[8].z)
                #print(image.shape)
                #create a circle on the finger tip ---------------------------
                cv2.circle(image, (x1,y1), 10, color, 5)
                #cv2.line(image, (0,0), (x1, y1), (0,0,0), 5)
                '''mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )'''
                
            
        #Add a circle to that cordinates------------------------------
                
        for i in range(len(points)):
            #print(points[i][0], points[i][1])
            
            #calculate distance between the points *IMP*
            
            dist = abs((points[i][0] - points[i-1][0]) + (points[i][1] - points[i-1][1]))
            tdist = points[i][2] - points[i-1][2]
            
            if (i > 0 and dist < 200 and tdist < 2):
                cv2.line(image, (int(points[i-1][0]), int(points[i-1][1])), (int(points[i][0]), int(points[i][1])),(121, 22, 76), 10)
            
            cv2.circle(image, (int(points[i][0]), int(points[i][1])), 1, (121, 22, 76), 1)
            
            
        #-------------------------------------------------------------
        
        
        #impliment pop
        
        '''if cv2.waitKey(10) & 0xFF == ord('r'):
            points = []
        
        if cv2.waitKey(10) & 0xFF == ord('u'):
            points.pop()
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break'''
            
        if cv2.waitKey(10) & keyboard.is_pressed("r"):
            points = []
            pointsmo = []
            
        if cv2.waitKey(10) & keyboard.is_pressed("u"):
            if(len(points) > 0):
                points.pop()
                
        
        if cv2.waitKey(10) & keyboard.is_pressed("q"):
            break
        
        
        #move----------------------------------------
        
        mvmSpeed = 50
        
        if cv2.waitKey(10) & keyboard.is_pressed("l"):
            for i in range(0, len(points)):
                points[i][0] += mvmSpeed
                
        if cv2.waitKey(10) & keyboard.is_pressed("j"):
            for i in range(0, len(points)):
                points[i][0] -= mvmSpeed
                
        if cv2.waitKey(10) & keyboard.is_pressed("k"):
            for i in range(0, len(points)):
                points[i][1] += mvmSpeed
                
        if cv2.waitKey(10) & keyboard.is_pressed("i"):
            for i in range(0, len(points)):
                points[i][1] -= mvmSpeed
        
        #---------------------------------------------
        
        #Rotation Code--------------------------------
        
        ##Calculate the center of the figure
        
        if cv2.waitKey(10) & keyboard.is_pressed("g"):
        
            sumx = 0
            sumy = 0
            f = 0
            
            for i in range(0, len(points)):
                sumx += points[i][0]
                sumy += points[i][1]
                f += 1
            
            sumx /= f
            sumy /= f
            
            cos = 0
            sin = 1

            
            #tmat = [[0, -1],[1, 0]]
            
            for i in range(0, len(points)):
                tx = points[i][0] 
                ty = points[i][1]
                
                tx -= sumx
                ty -= sumy
               
                temp = tx
                tx =  -ty
                ty = temp
                   
                #tx = cos*tx - sin*ty
                #ty = sin*tx + cos*ty
                
                tx += sumx
                ty += sumy
                
                #print(str(points[i][0])+" "+str(tx)+"__"+ str(points[i][1])+" "+str(ty))
                
                points[i][0] = tx 
                points[i][1] = ty
        
        #---------------------------------------------
        
        
                    
        cv2.imshow('Hand Tracking', image)
        
        '''To create both straight and curvy lines we will have to use two lists'''

cap.release()
cv2.destroyAllWindows()
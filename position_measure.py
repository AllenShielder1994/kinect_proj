from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

import numpy as np
import cv2
from cv2 import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

#######################################################################
#GREEN
lower_color_G=np.array([35,43,46])
upper_color_G=np.array([77,255,255])


#YELLOW
lower_color_Y=np.array([26,43,46])
upper_color_Y=np.array([34,255,255])

#RED
lower_color_R=np.array([156,43,46])
upper_color_R=np.array([180,255,255])

#BLUE
lower_color_B=np.array([100,43,46])
upper_color_B=np.array([124,255,255])

#Gitted_rid
lower_color_R_g=np.array([171,126,130])
upper_color_R_g=np.array([180,255,255])

######################################################################


#point_color = (0, 0, 255) #red
#point_color = (255, 0, 0) #blue
point_color = (0, 255, 0) #green

red = (0, 0, 255) #red
blue = (255, 0, 0) #blue
green = (0, 255, 0) #green

   
x_colllect =0
y_colllect =0
time =1
current_position =0




while not kinect.has_new_color_frame():
    a = None

while True:
    if kinect.has_new_color_frame():
        newImg = np.array(kinect.get_last_color_frame())
        newImg = newImg.reshape((1080,1920,4))
       # cv2.imshow("Kinect", newImg)
        # DO PROCESSING

        


        
        hsv = cv2.cvtColor(newImg, cv2.COLOR_BGR2HSV)

        # get mask
        mask = cv2.inRange(hsv, lower_color_R_g, upper_color_R_g)

        

        #cv2.namedWindow("Mask")


        cv2.imshow('Mask', mask)


        # detect color
        #res = cv2.bitwise_and(newImg, newImg, mask=mask)
        #cv2.imshow('Result', res)
        
        
        #cv2.circle(newImg, positon, 60, point_color, 0)

        #cv2.namedWindow("image")
        #cv2.imshow('image', newImg) 


        conts,hier = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)# find out edge
        cv2.drawContours(newImg,conts,-1,point_color,1)# show contours on monitor
        #dst = cv2.bitwise_and(newImg,newImg,mask=mask)#trake each picture
        #cv2.imshow ("dst",dst)
        cv2.imshow ("img_detect",newImg)

        for i in range(0,len(conts)):  
            x, y, w, h = cv2.boundingRect(conts[i])   
            cv2.rectangle(newImg, (x,y), (x+w,y+h), green, 2) 
            if cv2.waitKey(1) & 0xFF == ord('Q'):
                print(conts[i])
        
        check_time =18
        correction_value =5
        
        if time <check_time:
            #print (time)
            x_colllect = x_colllect + x
            # print (x_colllect,x)
            time=time+1

        else :
        # print ("result:")
            if ((x_colllect / check_time) < (current_position-correction_value)) or ((x_colllect / check_time) > (current_position+correction_value)):
                current_position = x_colllect/check_time
                #print (current_position, x_colllect)
                print (current_position)
                #print ("END:")
            x_colllect = 0
            time =1

        

        key =cv2.waitKey(1) #保持画面的持续。
        if key == ord ("Q"):
            if time <check_time:
                #print (time)
                x_colllect=x_colllect+x
                # print (x_colllect,x)
                time=time+1

            else :
                # print ("result:")
                print (x_colllect/check_time)
                #print ("END:")
                x_colllect = 0
                time =1


        elif key == ord ("W"):
            print ("**************************** END X",check_time, "****************************")
            break


        cv2.imshow("img",newImg)
        #print (conts)



    if cv2.waitKey(1)&0xff == 27:
        break 
    


# cv2.waitKey(0)

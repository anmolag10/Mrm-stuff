
You're using code navigation to jump to definitions or references.
Learn more or give us feedback
import cv2
import  numpy as np
m =0
aspect_ratio = 0
def nothing(x):
    pass
def save(x):
cap = cv2.VideoCapture(0)
while(True):
    z,frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lh = cv2.getTrackbarPos('lh', "HSV")
        ls = cv2.getTrackbarPos('ls', "HSV")
        lv = cv2.getTrackbarPos('lv', "HSV")
        uh = cv2.getTrackbarPos('uh', "HSV")
        hs = cv2.getTrackbarPos('hs', "HSV")
        hv = cv2.getTrackbarPos('hv', "HSV")
        a1 = cv2.getTrackbarPos('a1',"circle")
        a2 = cv2.getTrackbarPos('a2',"circle")
        e1 = cv2.getTrackbarPos('e1', "circle")
        e2 = cv2.getTrackbarPos('e2', "circle")
        minrad = cv2.getTrackbarPos('minrad',"circle")
        a1 = a1/100
        a2 = a2 / 100
        e1 = e1 / 100
        e2 = e2 / 100
        thresh1 = np.array([lh,ls,lv])
        thresh2 = np.array([uh,hs,hv])
        mask = cv2.inRange(HSV,thresh1,thresh2)

        kernel = np.ones((2,2),np.uint8)/4
        mask  = cv2.erode(mask,kernel,iterations=2)
        mask = cv2.dilate(mask,kernel,iterations=3)
        #mask = cv2.medianBlur(mask,5)

        image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
        HSV1 = cv2.bitwise_and(frame, frame, mask=mask)

        for i in range(0,len(contours)):
            if(len(contours)>1):
                (x,y),radius = cv2.minEnclosingCircle(contours[i])
                center = (int(x),int(y))
                radius = int(radius)
                x, y, w, h = cv2.boundingRect(contours[i])
                aspect_ratio = float(w) / h
                area1 = np.pi * radius * radius
                area2 = cv2.contourArea(contours[i])
                if(area1 != 0 and area2 != 0 ):
                    e = area1/area2
                else:
                    e = 0

            if(aspect_ratio > a1 and aspect_ratio < a2 and e>e1 and e < e2 and minrad<radius):
                HSV1 = cv2.circle(HSV1,center,radius,(0,0,255),2)
                print("BALL!!!!")
        else:
            pass
        cv2.imshow("HSV",HSV1)

        if(cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()


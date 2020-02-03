import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerball = np.array([25, 53, 61])
    upperball = np.array([61, 255, 255])
    kernal = np.ones((2, 2), np.uint8) / 4
    mask = cv2.inRange(hsv, lowerball, upperball)
    mask = cv2.erode(mask, kernal)
    mask = cv2.filter2D(mask, -1, kernal)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    resgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(resgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(contours)==1:
     for i in range (0,1000):
        kernel = np.ones((1,k),np.uint8)
        erosion = cv2.erode(thresh,kernel,iterations = 1)
        _, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        if len(contours) == 1:
            k+=1
        if len(contours) == 2:
            break
        if len(contours) > 2:
            print('more than one contour')

     x,y,w,h = cv2.boundingRect(contours[0])
     cv2.rectangle(threshold,(x-k,y-k),(x+w+k,y+h+k), 0, 1)
     _, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0,0,255), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    #`cv2.imshow("res", res)
    #cv2.imshow("hsv",hsv)
    key = cv2.waitKey(1)
    if key == 27:
        break
    cap.release()
    cv2.destroyAllWindows()

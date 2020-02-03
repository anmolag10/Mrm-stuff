import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Track")

cv2.createTrackbar("LH", "Track", 0, 255, nothing)
cv2.createTrackbar("LS", "Track", 0, 255, nothing)
cv2.createTrackbar("LV", "Track", 0, 255, nothing)
cv2.createTrackbar("UH", "Track", 255, 255, nothing)
cv2.createTrackbar("US", "Track", 255, 255, nothing)
cv2.createTrackbar("UV", "Track", 255, 255, nothing)

while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # hsv = cv2.GaussianBlur(hsv, (5, 5), 0)
    lh = cv2.getTrackbarPos("LH", "Track")
    ls = cv2.getTrackbarPos("LS", "Track")
    lv = cv2.getTrackbarPos("LV", "Track")

    uh = cv2.getTrackbarPos("UH", "Track")
    us = cv2.getTrackbarPos("US", "Track")
    uv = cv2.getTrackbarPos("UV", "Track")
    savekey =cv2.waitKey(1)
    if savekey==115:
        lowerball = np.array([lh, ls, lv])
        upperball = np.array([uh, us, uv])
        print(lowerball)
        print(upperball)

    lowerball = np.array([lh, ls, lv])
    upperball = np.array([uh, us, uv])
    kernal = np.ones((3, 3), np.uint8) /9
    mask = cv2.inRange(hsv, lowerball, upperball)
    mask = cv2.dilate(mask, kernal)
    mask=cv2.filter2D(mask,-1,kernal)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    resgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(resgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(res, contours, 0, (0, 0, 255), 3)
    rect = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(res, [box], 0, (0, 0, 255), 2)
    if((len(contours)>1)):
        (x,y), radius=cv2.minEnclosingCircle(contours[0])
        center=(int(x),int(y))
        radius=int(radius)
        res=cv2.circle(res,center,radius,(0,255,0))


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

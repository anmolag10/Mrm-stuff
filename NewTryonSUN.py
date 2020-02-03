import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
    hsv=cv2.GaussianBlur(hsv,(5,5),0)
    lowerball = np.array([30,46,93])
    upperball = np.array([85,139,255])
    mask = cv2.inRange(hsv, lowerball, upperball)
    kernel = np.ones((2, 2), np.uint8) / 4
    mask = cv2.erode(mask,kernel,iterations=2)
    mask = cv2.dilate(mask,kernel, iterations=4)
    res = cv2.bitwise_and(frame,frame,  mask = mask)

    conts,hierarchy= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = np.array(conts)
    if len(conts) > 0:
        for i, contour in enumerate(conts):
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            if(rect[1][1]==0):
                pass
            else:
                aratio = (rect[1][0] / rect[1][1])
                if (aratio > 0.9) and (aratio < 1.1):
                    cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)



            print("Aspect Ratio",aratio)



    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=255, param2=20, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:


            if (aratio > 0.9) and (aratio < 1.1):
                cv2.circle(res, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(res, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0), -1)










    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',hsv)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
import cv2
import numpy as np
conval=list()
k=2
hfval=list()
def nothing(x):
    pass
cap = cv2.VideoCapture(0);
aratio=1
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
    if len(contours) == 1:
      for i in range(0, 1000):
        kernel = np.ones((1, k), np.uint8)
        erosion = cv2.erode(thresh, kernel, iterations=1)
        contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        if len(contours) == 1:
            k += 1
        if len(contours) == 2:
            break
        if len(contours) > 2:
            print('more than one contour')
    for c in contours:
        m = cv2.moments(c)
        area = m['m00']
        if (area > 5000 and area < 15000):
            ((x1, y1), r1) = cv2.minEnclosingCircle(c)

            gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=20, minRadius=9, maxRadius=60)
            if circles is not None:

                detectedcircles = np.uint16(np.around(circles))
                for (x, y, r) in detectedcircles[0, :]:
                    if (((r / r1) > 0.88) and ((r / r1) < 1.1)):
                        cv2.circle(frame, (x, y), r, (0, 255, 255), 3)

                        cv2.putText(frame, '*BALL DETECTED*', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (25, 2, 100), 1)
                        print('Area:', np.pi * r * r)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    #`cv2.imshow("res", res)
    #cv2.imshow("hsv",hsv)
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
#MIGHT NOT WORK FOR MULTIPLE BALLS IN SOME SITUTATIONS

import cv2 as cv

import numpy as np
import threading
retl = False
retr = False
end = False

def capl():
    cap = cv.VideoCapture(2)
    global framel
    global retl
    while True:
        retl, framel = cap.read()
        if end==True:
            break

def capr():
    cap = cv.VideoCapture(0)
    global framer
    global retr
    while True:
        retr, framer = cap.read()
        if end==True:
            break

def main():
    global retr, retl
    while retr == False or retl == False:
        pass
    while True:

        cv.imshow('frame1', framel)
        cv.imshow('frame2', framer)
        key = cv.waitKey(1)
        if key == ord('q'):
            global end
            end = True
            break



tcl = threading.Thread(target=capl, args=())
tcr = threading.Thread(target=capr, args=())
tm = threading.Thread(target=main, args=())
tcl.start()
tcr.start()
tm.start()
if KeyboardInterrupt:
    end=True
    tcl.join()
    tcr.join()
    tm.join()

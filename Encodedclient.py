import socket
import pickle
import cv2
import numpy as np
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6000))
while 1:
    dframe = []
    while True:
        packet = s.recv(65535)
        if not packet:
            break
        dframe.append(packet)
        try:
            if(pickle.loads(packet) == "end"):
                break
        except:
            pass
    try:

        m,data = pickle.loads(b"".join(dframe))
        data = cv2.imdecode(data,-1)
        data= cv2.resize(data,(640,480))
        cv2.imshow('frame',data)
    except:
        pass
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cv2.destroyAllWindows()
s.close()
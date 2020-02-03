
import socket
import cv2
import numpy as np
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8000))
s.listen(3)
clt, adr= s.accept()

cap = cv2.VideoCapture(0)
while 1:
    _, frame = cap.read()
    l,b,ch=frame.shape
    frame = cv2.resize(frame, (int(b/ 2), int(l / 2)))
    frame = cv2.imencode('.jpeg', frame)


    frame_size = pickle.dumps(np.size(frame[1]))

    frame = pickle.dumps(frame)
    clt.sendall(frame_size)
    answer = clt.recv(8)
    clt.sendall(frame)

clt.close()
s.close()
cap.release()
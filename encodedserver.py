import socket
import cv2
import numpy as np
import pickle
import time

cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 150)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 6000))
sock.listen(5)
addr, clt = sock.accept()
time.sleep(4)
while (True):
    z, frame = cap.read()
    if z:
        frame = cv2.imencode('.jpg', frame,[cv2.IMWRITE_JPEG_QUALITY, 80])
        size=pickle.dumps(np.size(frame[1]))
        frame = pickle.dumps(frame)
        addr.sendall(frame)
        time.sleep(0.01)
        end= pickle.dumps("end")
        addr.sendall(end)
        #addr.sendall(size)
a.close()
cap.release()
cv2.destroyAllWindows()
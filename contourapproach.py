
import socket
import pickle
import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.43.159', 8000))

while 1:
    data = []
    size=0
    sizepacket=s.recv(8)
    frame_size=pickle.loads(sizepacket)
    print(frame_size)
    s.send(b'1')
    while size<=frame_size:
        packet = s.recv(65535)
        if not packet: break
        data.append(packet)
        size += len(packet)
    data_arr = pickle.loads(b"".join(data))
    data_arr = cv2.imdecode(data_arr[1],cv2.IMREAD_COLOR)
    print(data_arr.shape)
    cv2.imshow('frame',data_arr)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
s.close()

import cv2 
import numpy as np 
import socket
import struct

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',6000))
while True:
    data=b''
    size=(sock.recv(8))
    print(len(size))
    size=struct.unpack('L',size)

    while len(data)<size:
        data+=sock.recv(800000)
        sock.sendall('d')
        frame_encoded = np.fromstring(data, dtype='uint8')
        frame_encoded =  np.reshape(frame_encoded, (len(frame_encoded), 1))
        frame = cv2.imdecode(frame_encoded, -1)
        factor = 1.5
        
    frame = cv2.resize(frame, (int(640/2), int(480/2)))
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
            break

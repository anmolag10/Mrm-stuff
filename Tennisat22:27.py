import socket
import pickle
import cv2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))

while 1:
    data = []
    size=0
    sizepacket=s.recv(8)
    frame_size=pickle.loads(sizepacket)
    print(frame_size)
    s.send(b'end')
    while size<=frame_size:
        packet = s.recv(65535)
        if not packet: break
        data.append(packet)
        size += len(packet)
    data_arr = pickle.loads(b"".join(data))
    data_arr = cv2.imdecode(data_arr[1],cv2.IMREAD_ANYCOLOR)
    print(data_arr.shape)
    data_arr= cv2.resize(data_arr, (640, 480))
    cv2.imshow('frame',data_arr)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
s.close()
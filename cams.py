import cv2
import socket
import struct
import pickle
import constants

cap = cv2.VideoCapture(0)

#CAM 1: (front facing camera)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('PC2_IP_ADDRESS', constants.CAM_1_PORT))

def stream_cams():
    while True:
        ret, frame = cap.read()

        data = pickle.dumps(frame)
        message_size = struct.pack("L", len(data))

        client_socket.sendall(message_size + data)

        # This is optional, just to make sure its working
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()

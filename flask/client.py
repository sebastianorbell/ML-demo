"""
Name : client-camera.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 17:35
Desc:
"""

# import the necessary packages
import cv2
import imagezmq
import argparse
import socket
import time
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=False, default='127.0.0.1',
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())
# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
	args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
print('Connected to server ', "tcp://{}:5555".format(
	args["server_ip"]))
cap = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
    # read the frame from the camera and send it to the server
    # Capture frame-by-frame
    # This method returns True/False as well
    # as the video frame.
    ret, frame = cap.read()
    dim = (1080, 1080)
    resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    sender.send_image(rpiName, resized_frame)


# Close down the video stream
sender.zmq_socket.close()
cap.release()
cv2.destroyAllWindows()


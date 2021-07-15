"""
Name : server-stream.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 15/07/2021 11:40
Desc:
"""

import imagezmq
import cv2
import socket
import sys
import torch
import numpy as np
import os

from transferFunction import StyleClass

cwd = os.getcwd()
imageHub = imagezmq.ImageHub(open_port='tcp://*:5556')

def plot_frames():  # generate frame by frame from camera
    while True:
        (rpiName, frame) = imageHub.recv_image()
        imageHub.send_reply(b'OK')
        cv2.imshow('Live style transfer', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Close down the video stream
    cv2.destroyAllWindows()
    cv2.waitKey(1)


if __name__ == '__main__':
    local_ip = socket.gethostbyname('localhost')
    print('Server ip address ', local_ip)
    plot_frames()
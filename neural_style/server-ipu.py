"""
Name : server-ipu.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 15/07/2021 10:35
Desc:
"""
import imagezmq
import cv2
import socket
import sys
import torch
import numpy as np
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
ap.add_argument("-m", "--model", required=False, default=2,
	help="0-3 -- select which style to transfer")
args = vars(ap.parse_args())

from transferFunction import StyleClass

cwd = os.getcwd()

images_dir = cwd+'/images/'
models_dir = cwd+'/saved_models/'
sys.path.append(images_dir)
sys.path.append(models_dir)

styles = ['candy.pth', 'mosaic.pth', 'rain_princess.pth', 'udnie.pth']

modelpath = models_dir+styles[args['model']]

styleClass = StyleClass(modelpath)

function = lambda x: np.moveaxis(styleClass.stylize(torch.from_numpy(np.moveaxis(x, -1, 0).astype(np.float32))).numpy(),0,-1)

imageHub = imagezmq.ImageHub()

def gen_frames(function):  # generate frame by frame from camera
    while True:
        (rpiName, frame) = imageHub.recv_image()
        imageHub.send_reply(b'OK')

        new_frame = function(frame)
        norm_image = cv2.normalize(new_frame, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        sender = imagezmq.ImageSender(connect_to="tcp://{}:5556".format(
            args["server_ip"]))
        sender.send_image('ai comp', norm_image)

        # cv2.imshow('New Frame', norm_image)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    # Close down the video stream
    sender.zmq_socket.close()
    # cv2.destroyAllWindows()
    # cv2.waitKey(1)


if __name__ == '__main__':
    local_ip = socket.gethostbyname('localhost')
    print('Server ip address ', local_ip)
    gen_frames(function)
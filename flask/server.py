"""
Name : server.py.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 17:38
Desc:
"""

import numpy as np
import imagezmq
from flask import Flask, render_template, Response
import socket
import cv2
import os

app = Flask(__name__)


imageHub = imagezmq.ImageHub()

camera = cv2.VideoCapture(0)
def gen_frames():  # generate frame by frame from camera
    while True:
        (rpiName, frame) = imageHub.recv_image()
        imageHub.send_reply(b'OK')
        ret, frame = camera.read()
        ret, buffer = cv2.imencode('.jpg', frame)

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # do a bit of cleanup
    cv2.destroyAllWindows()


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    local_ip = socket.gethostbyname('localhost')
    print('Server ip address ', local_ip)
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT',8080)))
"""
Name : openCV.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 14:39
Desc:
"""

import cv2  # Import the OpenCV library
import numpy as np  # Import Numpy library

def online(function):
    """
    Main method of the program.
    """

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    while (True):

        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.
        ret, frame = cap.read()
        dim = (1080, 1080)
        resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        # Edit frame and return
        new_frame = function(resized_frame)
        norm_image = cv2.normalize(new_frame, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        cv2.imshow('New Frame', norm_image)

        # If "q" is pressed on the keyboard,
        # exit this loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close down the video stream
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':


    print(__doc__)
    online()
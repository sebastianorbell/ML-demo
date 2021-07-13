"""
Name : inAndOut.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 13/07/2021 14:47
Desc:
"""
import cv2  # Import the OpenCV library
import numpy as np  # Import Numpy library

def main(function):
    """
    Main method of the program.
    """

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Create the background subtractor object
    # Use the last 700 video frames to build the background
    # back_sub = cv2.createBackgroundSubtractorMOG2(history=700,
    #                                               varThreshold=25, detectShadows=True)

    # Create kernel for morphological operation
    # You can tweak the dimensions of the kernel
    # e.g. instead of 20,20 you can try 30,30.
    kernel = np.ones((20, 20), np.uint8)

    while (True):

        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.
        ret, frame = cap.read()

        # Edit frame and return
        new_frame = function(frame)
        cv2.imshow('New Frame', new_frame)

        # If "q" is pressed on the keyboard,
        # exit this loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close down the video stream
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print(__doc__)
    main()
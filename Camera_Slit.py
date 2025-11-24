# This is the vision library OpenCV
import cv2
# This is a library for mathematical functions for python (used later)
import numpy as np
# This is a library to get access to time-related functionalities
import time
# This is the Aruco library from OpenCV
import cv2.aruco as aruco 
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

Camera=np.load('Sample_Calibration.npz') #Load the camera calibration values 
CM=Camera['CM'] #camera matrix 
dist_coef=Camera['dist_coef']# distortion coefficients from the camera 


# Select the first camera (0) that is connected to the machine
# in Laptops should be the build-in camera
cap = cv2.VideoCapture(0)
 
# Set the width and heigth of the camera to 1920x1080
cap.set(3,1920)
cap.set(4,1080)

#Create frame and slit opencv named windows
cv2.namedWindow("frame-image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("slit-image", cv2.WINDOW_AUTOSIZE)

#Position the windows ontop of eachother
cv2.moveWindow("frame-image",0,100)
cv2.moveWindow("slit-image",635,100)

# Execute this continuously
while(True):
    
    # Start the performance clock
    start = time.perf_counter()
    
    # Capture current frame from the camera
    ret, frame = cap.read()

    # --- central slit extraction ---
    # Change this value to control how many pixels wide the slit is
    SLIT_Height = 5  # pixels (odd number keeps perfect centering)

    # image dimensions
    w, h = frame.shape[:2]
    cy = h // 2
    half = SLIT_Height // 2
    # y0 = max(cy - half, 0)
    # y1 = min(cy + half + (SLIT_Height % 2), h)
    y0 = cy - half
    y1 = cy + half

    # extract a thin vertical slit centered horizontally
    slit_frame = frame[:, y0:y1]
    # small visualization helper: stretch slit horizontally for display
    # slit_vis = cv2.resize(slit_gray, (w, 200), interpolation=cv2.INTER_NEAREST)
    # --- end slit extraction ---

    # Display the original full frame in a window
    cv2.imshow('frame-image', frame)
    cv2.imshow('slit-image', slit_frame)

    # Stop the performance counter
    end = time.perf_counter()
    
    # Print to console the execution time in FPS (frames per second)
    fps = 1.0 / (end - start) if end > start else 0.0
    logging.info("FPS: %.1f", fps)

    # If the button q is pressed in one of the windows 
    if cv2.waitKey(20) & 0xFF == ord('q'):
        # Exit the While loop
        break
    

# When everything done, release the capture
cap.release()
# close all windows
cv2.destroyAllWindows()
# exit the kernel
exit(0)
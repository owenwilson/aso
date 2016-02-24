import cv2, platform
#import numpy as np

#cam = "mmst://192.168.1.147:8080/?action=stream"
#cam = 0 # Use  local webcam.
cap=cv2.VideoCapture("http://192.168.1.1:2222/javascript_simple.html")

while(True):
    # Capture frame-by-frame
    ret, current_frame = cap.read()
    if type(current_frame) == type(None):
        print("!!! Couldn't read frame!")
        break

    # Display the resulting frame
    cv2.imshow('frame',current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()

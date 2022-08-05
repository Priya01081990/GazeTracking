
from datetime import datetime
from gaze_tracking import GazeTracking
import cv2
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # get a new frame from the webcam
    _, frame = webcam.read()

    # send this frame to GazeTracking
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"


    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"simple-EYE-Tracker@{current_time}:", text)
    left_pupil = gaze.pupil_left_coords()
    print(f"simple-EYE-Tracker@{current_time}:", "Left_Puipl_XY",  left_pupil)
    right_pupil = gaze.pupil_right_coords()
    print(f"simple-EYE-Tracker@{current_time}:", "Right_Puipl_XY", right_pupil)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27: # press escape to to exit
        break
   
webcam.release()
cv2.destroyAllWindows()

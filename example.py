timport cv2
from gaze_tracking import GazeTracking
from pynput.mouse import Button, Controller

mouse = Controller()

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = ""
    text2 = ""
    text3 = ""

    if gaze.is_blinking():
        text1 = "Blinking"
    elif gaze.is_right():
        text1 = "Right"
        mouse.move(5, 0)
    elif gaze.is_left():
        text1 = "Left"
        mouse.move(-5, 0)
    elif gaze.is_center():
        text1 = "Center"
    if gaze.is_down():
        text2 = "Down"
        mouse.move(0, 5)
    elif gaze.is_up():
        text2 = "Up"
        mouse.move(0, -5)
    if gaze.left_blink():
        text3 = "Left Blink"
        mouse.click(Button.left)
    elif gaze.right_blink():
        text3 = "Right Blink"
        mouse.click(Button.right)


    cv2.putText(frame, text1 + "+" + text2 + "+" + text3, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 330), cv2.FONT_HERSHEY_DUPLEX, 0.7, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 365), cv2.FONT_HERSHEY_DUPLEX, 0.7, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()

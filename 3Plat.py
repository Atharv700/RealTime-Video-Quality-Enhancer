import pyautogui
import cv2
import numpy as np

def mouse_event(event, x, y, flags, param):
    pass   

screen_width, screen_height = pyautogui.size()

capture_region = (0, int(0.5 * screen_height), int(0.5 * screen_width), int(0.5 * screen_height))
display_region = (int(0.5 * screen_width), 0, int(0.5 * screen_width), int(0.5 * screen_height))

while True:
    img = pyautogui.screenshot(region=capture_region)

    capture_frame = np.array(img)
    capture_frame = cv2.cvtColor(capture_frame, cv2.COLOR_RGB2BGR)

    capture_frame = cv2.convertScaleAbs(capture_frame, alpha=1.5, beta=0)

    img = pyautogui.screenshot(region=display_region)

    display_frame = np.array(img)
    display_frame = cv2.cvtColor(display_frame, cv2.COLOR_RGB2BGR)

    cv2.imshow("Screen Recording", np.hstack([capture_frame, display_frame]))

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

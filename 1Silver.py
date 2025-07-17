import pyautogui
import cv2
import numpy as np


screen_width, screen_height = pyautogui.size()


capture_region = (0, int(0.5 * screen_height), int(0.5 * screen_width), int(0.5 * screen_height))
display_region = (int(0.5 * screen_width), 0, int(0.5 * screen_width), int(0.5 * screen_height))


interpolation = cv2.INTER_LINEAR

while True:
  
    img = pyautogui.screenshot(region=capture_region)

    
    capture_frame = np.array(img)
    capture_frame = cv2.cvtColor(capture_frame, cv2.COLOR_RGB2BGR)

    capture_frame = cv2.resize(capture_frame, (1280, 720), interpolation=interpolation)

    capture_frame = cv2.resize(capture_frame, (display_region[2], display_region[3]), interpolation=interpolation)

    cv2.imshow("Screen Recording", capture_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

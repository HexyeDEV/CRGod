import numpy as np
from PIL import ImageGrab, Image
import cv2
import time

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 400, 750)))

    print(f"Frame took {time.time() - last_time:.2f} seconds")
    last_time = time.time()

    cv2.imshow("Screen Capture", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
import cv2
from mss.windows import MSS as mss
import numpy as np
import pyautogui as pg
import time
from find_dino import find_dino


def main():
    sct = mss()
    pg.PAUSE = 0
    pos = find_dino()
    jump_time = 0 


    while True:
        img = np.array(sct.grab(pos))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 250, 255)
        edges_sum = np.sum(edges)

        cv2.imshow("img", edges)                                                                                                                                                                                                                                    

        if edges_sum > 4000:
            pg.keyDown('space')
            jump_time = time.time()

    
        if time.time() - jump_time > 0.08:
            pg.keyUp('space')

    
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
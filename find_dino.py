import cv2
from mss.windows import MSS as mss
import numpy as np
import pyautogui as pg


def find_dino():
    sct = mss()
    pg.PAUSE = 0
    found = 0

    while not found:
        print("Searching for dinos...")
        dino_img = cv2.imread("dino.png")
        template = cv2.imread(sct.shot())

        res = cv2.matchTemplate(dino_img, template, cv2.TM_CCOEFF_NORMED)
        pos = np.where(res > 0.95)


        for pt in zip(*pos[::-1]):
            x, y = pt
            
            if x and y or x == 0 and y or x and y == 0:
                found = 1
    
    pos = {
        "top" : y-12,
        "left" : x+50,
        "width" : 75,
        "height" : 40
    }

    return pos
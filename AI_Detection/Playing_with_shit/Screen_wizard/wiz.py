import cv2
import time
import pyautogui as pag
from Modules.handjob import *
from PIL import ImageGrab

# Hold Hand up for 3 seconds and then check movement
active = False
avg = 0
starttime = 0
center = 0


def move_page(center, new_center):
    if (math.dist(center, new_center) > 200):
        if (center[0] < new_center[0]):
            pag.hotkey('ctrl', 'right', interval=0.1)
        else:
            pag.hotkey('ctrl', 'left', interval=0.1)


funcs = [
    handup,
    pointer_up
]


try:
    move_cursor = False
    func = handup
    while True:

        if not active:
            for f in funcs:
                if f():
                    starttime = time.time()
                    active = True
                    center = get_center()
                    func = f

        if not func() and active:
            active = False

        if func() and active and (time.time() - starttime > 2):
            new_center = get_center()

            if func == handup:
                move_page(center, new_center)
            elif func == funcs[1]:
                move_cursor = True

        if move_cursor:
            coords = get_finger_coord("pointer", False)
            w, h = pag.size()
            try:
                pag.moveTo((1-coords.x)*w, coords.y*h, 0.3, pag.easeInOutQuad)
                pag.mouseDown() if pinch() else pag.mouseUp()

            except:
                move_cursor = False

        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break
except KeyboardInterrupt:
    close_cap()

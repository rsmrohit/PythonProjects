import cv2 as cv
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(param['img'], (x, y), param['size'], (255, 0, 0), -1)

# Draws a circle on button click on a black canvase when used with draw_circle method
# just trying out mouse events


def draw_on_canvas(functioncall):
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')

    param = {'img': img, 'size': 50}
    cv.setMouseCallback('image', functioncall, param)

    while (True):
        cv.imshow('image', img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()


def videotest():
    cap = cv.VideoCapture(0)

    # cv.namedWindow('VideoCap')
    # param = {'img': np.zeros((512, 512, 3), np.uint8), 'size': 50}
    # cv.setMouseCallback('VideoCap', draw_circle, param)

    if not cap.isOpened():
        print("Camera cant be opened")
        exit()

# DEFAULT is 720 x 1280
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

    # if frame is read correctly ret is True
        if not ret:
            print("cant receive frame")
            break
    # operate on frame using frame object
    # X is first dimension where 0,0 is top left
    # cv.circle(frame, (360, 640), 20, (0, 0, 255), -1)
    # cv.circle(frame, (150, 300), 20, (0, 0, 255), -1)
        # param = {'img': frame, 'size': 50}

        cv.imshow('VideoCap', frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


videotest()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def grab_image():
    if not cap.isOpened():
        print("Cap not opened")  # NOTE: Change to logging later
        return False, None
    success, image = cap.read()

    if not success:
        print("Can't read")  # NOTE: Change to logging later
        return False, None

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return True, image


try:
    while True:

        succ, img = grab_image()
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if not succ:
            continue

        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)

        cv2.imshow("Window", img)

        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break

except KeyboardInterrupt:
    cap.release()

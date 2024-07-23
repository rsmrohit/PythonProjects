import cv2
import mediapipe as mp
import numpy as np
from typing import List, Mapping, Optional, Tuple, Union
import math
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.3,
    max_num_hands=4)

# Convertion!!


def _normalized_to_pixel_coordinates(
        normalized_x: float, normalized_y: float, image_width: int,
        image_height: int) -> Union[None, Tuple[int, int]]:
    """Converts normalized value pair to pixel coordinates."""

    # Checks if the float value is between 0 and 1.
    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                          math.isclose(1, value))

    if not (is_valid_normalized_value(normalized_x) and
            is_valid_normalized_value(normalized_y)):
        # TODO: Draw coordinates even if it's outside of the image bounds.
        return None
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px

# Method which will take in the landmarks and return if the pointer is pointing up
# NEED CONVERTED LANDMARKS


def finger_up(landmarks):
    pointer = landmarks[8]
    pointer_joint = landmarks[6]  # [x, y]

    if not (pointer and pointer_joint):
        return False

    if ((pointer[0] - pointer_joint[0]) == 0):
        return False

    if ((pointer[1] - pointer_joint[1]) / (pointer[0] - pointer_joint[0])) < -0.3:
        return True
    return False

# TODO: Make Two methods and dictionaries, one for all the finger landmarks so we can call specific finger when we want
# Second method is to take in the position of the finger and return its state
# Option third method: link the second one and first one to create full hand movements


# PART ONE: DICT OF FINGEYS from top to down
fin_marks = {
    "thumb": [4, 3, 2],
    "pointer": [8, 7, 6, 5],
    "middle": [12, 11, 10, 9],
    "ring": [16, 15, 14, 13],
    "pinky": [20, 19, 18, 17]
}

fin_pos = {

}

# This was a single method written to test the pyautogui and hands off screen control


def slope(p1, p2):
    if (p1[0] - p2[0]) == 0:
        return False
    return ((p1[1] - p2[1]) / (p1[0] - p2[0]))


def is_higher(p1, p2):
    if p1 == None or p2 == None:
        return False
    return p1[1] < p2[1]


def pinch():
    succ, ldm = get_landmark()

    if not succ:
        return False

    try:
        dist = math.dist(ldm[4], ldm[8])
        if dist < 40:  # TODO: Make it so that it is proportional to handsize
            # print(dist)
            return True
        else:
            return False
    except:
        return False

# Checks custom position for each finger


def get_finger_pos(finger):
    if finger not in fin_marks:
        return False

    xor = fin_marks[finger]

    succ, ldm = get_landmark()
    if not succ:
        return False

    for c in xor:
        if ldm[c] == None:
            return False

    if ldm[0] == None:
        return False

    # Condition is going to be bent if in between and direction
    edge = "und"

    xy = 1
    if abs(ldm[xor[0]][0] - ldm[xor[3]][0]) > abs(ldm[xor[0]][1] - ldm[xor[3]][1]):
        xy = 0

    if (ldm[xor[1]][xy] > ldm[xor[0]][xy] > ldm[xor[3]][xy]) or (ldm[xor[1]][xy] < ldm[xor[0]][xy] < ldm[xor[3]][xy]):
        edge = "middle"
    else:
        if abs(ldm[xor[0]][xy]-ldm[0][xy]) < abs(ldm[xor[2]][xy]-ldm[0][xy]):
            edge = "in"
        else:
            edge = "out"

    direction = ""

    if ldm[xor[0]][1] < ldm[0][1]:
        direction = "up"
    elif ldm[xor[0]][1] > ldm[0][1]:
        direction = "down"

    return (edge, direction)

# TODO: change return False into return None, because it makes more sense


def get_finger_coord(finger, normalize=True):
    if finger not in fin_marks:
        return False

    xor = fin_marks[finger]

    succ, ldm = get_landmark(normalize=normalize)
    if not succ:
        return False

    return ldm[xor[0]]

# ALL FOUR FINGERS ARE UP


def handup(landmarks=None):
    if landmarks == None:
        succ, landmarks = get_landmark()

        if not succ:
            return False

    for finger in fin_marks:

        if not fin_marks[finger][0] and fin_marks[finger][2]:
            return False

        if not is_higher(landmarks[fin_marks[finger][0]], landmarks[fin_marks[finger][2]]):
            return False
    return True


def pointer_up():
    cases = {"pointer": ("out", "up"),
             "middle": ("in", "up"),
             "ring": ("in", "up"),
             "pinky": ("in", "up"), }

    for c in cases:
        if get_finger_pos(c) != cases[c]:
            return False
    return True


def get_center(landmarks=None):
    if landmarks == None:
        succ, landmarks = get_landmark()

        if not succ:
            return False

    return (sum(landmarks[x][0] for x in range(4, 21, 4))/5, sum(landmarks[x][1] for x in range(4, 21, 4))/5)

# while get image from webcam using cv2


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

# Returns the hand that is closest to z in terms of distance (distance calculated by longest pointer len)
# RETURNS CONVERTED LANDMARKS


def get_landmark(image=None, z=0, normalize=True):
    if type(image) == type(None):
        succ, image = grab_image()
        if not succ:
            return False, None

    results = hands.process(image)
    image_rows, image_cols, _ = image.shape
    chosen_hand, long_len = None, 0
    if not results.multi_hand_landmarks:
        return False, None
    for hand in results.multi_hand_landmarks:
        tip = hand.landmark[8]
        tip0_px = _normalized_to_pixel_coordinates(
            tip.x, tip.y, image_cols, image_rows)

        tip = hand.landmark[6]
        tip1_px = _normalized_to_pixel_coordinates(
            tip.x, tip.y, image_cols, image_rows)

        if not (tip0_px and tip1_px):
            return False, None

        dist = math.dist(tip0_px, tip1_px)

        if long_len < dist:
            chosen_hand = hand
            long_len = dist

    if normalize:
        return True, [
            _normalized_to_pixel_coordinates(
                tip.x, tip.y, image_cols, image_rows
            ) for tip in chosen_hand.landmark
        ]
    else:
        return True, [
            tip for tip in chosen_hand.landmark
        ]

# Testing method, displays image and the landmark positions specified
# Landmark pos: list of integers of the positions wanting to be displayed
# NEEDS CONVERTED LANDMARKS


def show_image_landmarks(image, landmarks, landmark_pos=[0]):

    for landmark in landmark_pos:
        if not landmarks:
            break

        point = landmarks[landmark]  # [x, y]
        if not point:
            continue
        cv2.circle(image, (point[0], point[1]), 3, (0, 0, 0), -1)

    return image


def close_cap():
    cap.release()


if __name__ == "__main__":
    finger = False
    while True:
        succ, img = grab_image()

        # kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        # img = cv2.filter2D(img, -1, kernel)

        succ, res = get_landmark(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if not succ:
            continue

        img = show_image_landmarks(img, res, [8, 7, 6, 5])

        if finger != handup(res):
            finger = handup(res)

        # print("UP" if finger else "DOWN")
        cv2.putText(img, str(pointer_up()),
                    tuple(res[8]), 1, 1, (0, 0, 0))

        cv2.imshow("Window", img)

        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break

    cap.release()

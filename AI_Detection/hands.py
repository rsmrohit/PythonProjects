import drawing_utils_mine as mp_drawing
import cv2
import mediapipe as mp
import numpy as np
import drawMethods as dm
# mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh

draw_lines = True
draw_dots = True

color = [10, 90, 50]
change = [1, 0, -1]
send = np.zeros((720, 1280, 3))

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.3,
        min_tracking_confidence=0.3,
        max_num_hands=4) as hands:
    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=2,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        result_face = face_mesh.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            if len(results.multi_hand_landmarks) > 1:
                hand0 = results.multi_hand_landmarks[0]
                hand1 = results.multi_hand_landmarks[1]

                image_rows, image_cols, _ = send.shape
                tips = [8]

                if hand1 and hand0:
                    for i in tips:
                        tip0 = hand0.landmark[i]
                        tip1 = hand1.landmark[i]

                        tip0_px = mp_drawing._normalized_to_pixel_coordinates(
                            tip0.x, tip0.y, image_cols, image_rows)
                        tip1_px = mp_drawing._normalized_to_pixel_coordinates(
                            tip1.x, tip1.y, image_cols, image_rows)

                        # if tip0_px and tip1_px:
                        #     dm.lightning(send, tip0_px, tip1_px)

        # DRAWING HANDS
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # # CUSTOM DRAW LINE FROM 4 - 8 (TIP THUMB TO INDEX)
                # image_rows, image_cols, _ = send.shape
                # if hand_landmarks:
                #     thumb_tip = hand_landmarks.landmark[4]
                #     index_tip = hand_landmarks.landmark[8]

                #     thumb_px = mp_drawing._normalized_to_pixel_coordinates(
                #         thumb_tip.x, thumb_tip.y, image_cols, image_rows)
                #     index_px = mp_drawing._normalized_to_pixel_coordinates(
                #         index_tip.x, index_tip.y, image_cols, image_rows)

                #     if thumb_px and index_px:

                #         dm.lightning(send, thumb_px, index_px)

                mp_drawing.draw_landmarks(
                    image,
                    (hand_landmarks if draw_dots else None),
                    (mp_hands.HAND_CONNECTIONS if draw_lines else None),
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # if result_face.multi_face_landmarks:
        #     for face_landmarks in result_face.multi_face_landmarks:
        #         mp_drawing.draw_landmarks(
        #             image=send,
        #             landmark_list=face_landmarks,
        #             connections=mp_face_mesh.FACEMESH_TESSELATION,
        #             landmark_drawing_spec=None,
        #             connection_drawing_spec=mp_drawing_styles
        #             .get_default_face_mesh_tesselation_style())
        #         mp_drawing.draw_landmarks(
        #             image=send,
        #             landmark_list=face_landmarks,
        #             connections=mp_face_mesh.FACEMESH_CONTOURS,
        #             landmark_drawing_spec=None,
        #             connection_drawing_spec=mp_drawing_styles
        #             .get_default_face_mesh_contours_style())
        #         mp_drawing.draw_landmarks(
        #             image=send,
        #             landmark_list=face_landmarks,
        #             connections=mp_face_mesh.FACEMESH_IRISES,
        #             landmark_drawing_spec=None,
        #             connection_drawing_spec=mp_drawing_styles
        #             .get_default_face_mesh_iris_connections_style())

        # Flip the image horizontally for a selfie-view display

        for idx, x in enumerate(color):
            if idx == 1:
                pass
            if x > 50:
                change[idx] = -1
            if x < 10:
                change[idx] = 1
        # color = np.add(color, change)

        # send = np.subtract(send, color) # Decrease the color
        send[send < 0] = 0
        send = send.astype(np.uint8)
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        send = np.zeros((720, 1280, 3))
        key = cv2.waitKey(5) & 0xFF
        if key == 27:
            break
        elif key == 49:
            pass
            # print(results.multi_hand_landmarks[0]["landmark"])

        elif key == 50:
            draw_lines = not draw_lines
            print("draw_lines = " + str(draw_lines))
cap.release()

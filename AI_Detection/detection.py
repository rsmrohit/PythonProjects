# @markdown We implemented some functions to visualize the object detection results. <br/> Run the following cell to activate the functions.
from mediapipe.tasks.python import vision
from mediapipe.tasks import python
import mediapipe as mp
import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red


def visualize(
    image,
    detection_result
) -> np.ndarray:
    """Draws bounding boxes on the input image and return it.
    Args:
      image: The input RGB image.
      detection_result: The list of all "Detection" entities to be visualize.
    Returns:
      Image with bounding boxes.
    """
    for detection in detection_result.detections:
        # Draw bounding_box
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

        # Draw label and score
        category = detection.categories[0]
        category_name = category.category_name
        probability = round(category.score, 2)
        result_text = category_name + ' (' + str(probability) + ')'
        text_location = (MARGIN + bbox.origin_x,
                         MARGIN + ROW_SIZE + bbox.origin_y)
        cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

    return image


IMAGE_FILE = 'image.jpg'


img = cv2.imread(IMAGE_FILE)
cv2.imshow('HOLA', img)

# STEP 1: Import the necessary modules.

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(
    model_asset_path='lite-model_object_detection_mobile_object_localizer_v1_1_metadata_2.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.7)
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file(IMAGE_FILE)

# STEP 4: Detect objects in the input image.
detection_result = detector.detect(image)

# STEP 5: Process the detection result. In this case, visualize it.
image_copy = np.copy(image.numpy_view())
annotated_image = visualize(image_copy, detection_result)
rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

while (True):
    cv2.imshow('image', rgb_annotated_image)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

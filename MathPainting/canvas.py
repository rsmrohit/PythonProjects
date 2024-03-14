import numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height, color) -> None:
        self.data = np.zeros((width, height, 3), dtype=np.uint8)
        self.data[:] = color

    def make_image(self, image_filepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_filepath)
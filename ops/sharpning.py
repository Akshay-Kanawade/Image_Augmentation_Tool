import cv2
import numpy as np

CODE = 'sharp'


class Sharp:
    def __init__(self):
        self.code = CODE

    def process(self, img):
        sharp = np.array([[-1, -1, -1], [-1, -10, -1], [-1, -1, -1]])
        return cv2.filter2D(img, -1, sharp)

    @staticmethod
    def match_code(code):
        if code == CODE:
            return Sharp()

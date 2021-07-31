import cv2
import re
import random
import numpy as np
from cv2 import getAffineTransform

CODE = 'brightness'
REGEX = re.compile(r"^" + CODE + "_(?P<x_trans>[-0-9]+)_(?P<y_trans>[-0-9]+)")


class brightness:
    def __init__(self, x_trans, y_trans):
        self.code = CODE + str(x_trans) + '_' + str(y_trans)
        self.x_trans = x_trans
        self.y_trans = y_trans

    def process(self, img):
        value = random.uniform(self.x_trans, self.y_trans)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = np.array(hsv, dtype=np.float64)
        hsv[:, :, 1] = hsv[:, :, 1] * value
        hsv[:, :, 1][hsv[:, :, 1] > 255] = 255
        hsv[:, :, 2] = hsv[:, :, 2] * value
        hsv[:, :, 2][hsv[:, :, 2] > 255] = 255
        hsv = np.array(hsv, dtype=np.uint8)
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return img

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return brightness(int(d['x_trans']), int(d['y_trans']))

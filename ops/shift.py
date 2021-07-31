import cv2
import re
import random
import numpy as np
from cv2 import getAffineTransform

CODE = 'Shift'
REGEX = re.compile(r"^" + CODE + "_(?P<value>[-0-9]+)")


class Shift:
    def __init__(self, value):
        self.code = CODE + str(value)
        self.value = value

    def process(self, img):
        value = int(random.uniform(-self.value, self.value))
        img = img + value
        img[:, :, :][img[:, :, :] > 255] = 255
        img[:, :, :][img[:, :, :] < 0] = 0
        img = img.astype(np.uint8)
        return img


    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Shift(int(d['value']))

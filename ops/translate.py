import cv2
import re
from cv2 import getAffineTransform

CODE = 'trans'
REGEX = re.compile(r"^" + CODE + "_(?P<x_trans>[-0-9]+)_(?P<y_trans>[-0-9]+)")


class Translate:
    def __init__(self, x_trans, y_trans):
        self.code = CODE + str(x_trans) + '_' + str(y_trans)
        self.x_trans = x_trans
        self.y_trans = y_trans

    def process(self, img):
        row, col, c = img.shape
        return cv2.warpAffine(img, getAffineTransform(-self.x_trans, -self.y_trans), (col, row))

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Translate(int(d['x_trans']), int(d['y_trans']))

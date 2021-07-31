import cv2
CODE = 'gray'


class Gray:
    def __init__(self):
        self.code = CODE

    def process(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def match_code(code):
        if code == CODE:
            return Gray()

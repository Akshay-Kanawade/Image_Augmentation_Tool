import re
import cv2
import numpy as np
CODE = 'noise'
REGEX = re.compile(r"^" + CODE + "_(?P<var>[.0-9]+)")


def mat2gray(img):
    A = np.double(img)
    out = np.zeros(A.shape, np.double)
    normalized = cv2.normalize(A, out, 1.0, 0.0, cv2.NORM_MINMAX)
    return out


def random_noise(image, mode='gaussian', seed=None, clip=True, **kwargs):
        image = mat2gray(image)

        mode = mode.lower()
        if image.min() < 0:
            low_clip = -1
        else:
            low_clip = 0
        if seed is not None:
            np.random.seed(seed=seed)

        if mode == 'gaussian':
            noise = np.random.normal(kwargs['mean'], kwargs['var'] ** 0.5,
                                     image.shape)
            out = image + noise
        if clip:
            out = np.clip(out, low_clip, 1.0)

        return out


class Noise:
    def __init__(self, var):
        self.code = CODE + str(var)
        self.var = var

    def process(self, img):
        return random_noise(img, mode='gaussian', var=self.var, mean=0.1)

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Noise(float(d['var']))

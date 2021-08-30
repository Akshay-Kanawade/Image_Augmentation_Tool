# import library
import cv2
import numpy as np


def Read(image_path):
    """
    This function basically used to read the image.It read images in form of numpy array.
    :param image_path: source image
    :return: ndarray
    """
    # use cv2.imread()  to read an images.
    # syntax : cv2.imread(filename, flag=None)
    return cv2.imread(image_path, 0)


def Noise(img):
    """
    This function is used for detecting edges by using canny edge detection method .
    :param img: ndarray
    :return: image
    """
    noise_image = cv2.blur(img, (7, 7))
    # use np.array() to add noise on image
    return np.array(255 * noise_image)


def Show(orignal_img, noise_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param noise_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Noise_Image", noise_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# main function
def main():
    """
    This is main function used to call other function
    :return: nothing
    """
    image_path = input("Enter path of image:")
    # call read function to read an image
    img = Read(image_path)
    # call Noise() function to add noise on image
    noise_image = Noise(img)
    # call show function to show  original image and noise image
    Show(img, noise_image)


if __name__ == "__main__":
    main()

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
    return cv2.imread(image_path)


def Normalize(img):
    """
    This function is used to normalize the image as per the given norm method.
    :param img: ndarray
    :return: normalize image
    """
    norm = np.zeros((img.shape[1], img.shape[0]))
    return cv2.normalize(img, norm, 255, 0, cv2.NORM_MINMAX)


def Show(orignal_img, normalize_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param normalize_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Normalize_Image", normalize_image)
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
    # call normalize function to normalize image
    normalize_image = Normalize(img)
    # call show function to show  original image and resized image
    Show(img, normalize_image)


if __name__ == "__main__":
    main()

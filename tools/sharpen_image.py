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


def Sharp(img):
    """
    This method is used to sarp the image by applying filters.
    :param img: ndarray
    :return: sharpen image
    """
    # use cv2.sharp() function to sharp image
    # syntax : cv2.filter2D(src, depth, kernel)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)


def Show(orignal_img, sharp_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param sharp_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Sharp_Image", sharp_image)
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
    # call flip function to sharp the image
    sharp_image = Sharp(img)
    # call show function to show  original image and sharp image
    Show(img, sharp_image)


if __name__ == "__main__":
    main()

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


def Translate(img, x, y):
    """
   This function  is used for translate the image.
   :param img: ndarray
   :param x: int - x translation value
   :param y: int - y translation value
   :return: translated image
   """
    # use cv2.wrapAffine() function to apply affine translation on image
    # syntax : cv2.wrapAffine(src, m, dsize )
    rows, cols, c = img.shape
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, M, (cols, rows))


def Show(orignal_img, translated_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param translated_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Translated_Image", translated_image)
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
    # give threshold value
    x, y = map(int, input("enter valu -x -> left, -y -> up, x -> right, y -> down  for translation:").split(" "))
    # call translate function to translate image in x and y direction
    translated_image = Translate(img, x, y)
    # call show function to show  original image and edge translated image
    Show(img, translated_image)


if __name__ == "__main__":
    main()

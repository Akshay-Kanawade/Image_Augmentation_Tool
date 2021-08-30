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


def Negative(img):
    """
    This function is used to get negative image from orignal image.
    :param img: ndarray
    :return: image
    """
    S = 255
    shape = img.shape
    if shape[2] == "rgb":
        B, G, R = cv2.split(img)
        B[:] = [S - x for x in B]  # inverting blue
        G[:] = [S - x for x in G]  # inverting green
        R[:] = [S - x for x in R]  # inverting red
        # use cv2.merge() function to merge image
        # syntax : cv2.merge(src)
        return cv2.merge((B, G, R))
    else:
        # open in grayscale
        return np.array([S - x for x in img])


def Show(orignal_img, negative_image):
    """
    show the images
    :param orignal_img: orignal input image
    :param negative_image: inverted image
    :return: nothing
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Negative_Image", negative_image)
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
    # call negative function to invert image
    negative_image = Negative(img)
    # call show function to show  original image and negative_image
    Show(img, negative_image)


if __name__ == "__main__":
    main()

# import library
import cv2


def Read(image_path):
    """
    This function basically used to read the image.It read images in form of numpy array.
    :param image_path: source image
    :return: ndarray
    """
    # use cv2.imread()  to read an images.
    # syntax : cv2.imread(filename, flag=None)
    return cv2.imread(image_path)


def Invert(img):
    """
    inverted to invert the orignal image.
    :param img: ndarray
    :return: dilated image
    """
    # use cv2.bitwise_not to invert image
    # syntax : cv2.bitwise_not(src)
    return cv2.bitwise_not(img)


def Show(orignal_img, invert_img):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param invert_img: ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("invert_image", invert_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# main function
def main():
    """
    This is main function used to call other function
    :return: nothing
    """
    image_path = "1.jpg"
    # call read function to read an image
    img = Read(image_path)
    # call invert function to invert the image
    invert_img = Invert(img)
    # call show function to show  original image and dilate image
    Show(img, invert_img)


if __name__ == "__main__":
    main()

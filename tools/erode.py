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


def Erode(img):
    """
    erode is used to remove pixel on object boundaries.
    :param img: ndarray
    :return: eroded img
    """
    # use cv2.erode() function to flip image
    # syntax : cv2.erode(src, kernel, iterations)
    return cv2.erode(img, (7, 7), iterations=5)


def Show(orignal_img, erode_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param erode_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Erode_Image", erode_image)
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
    # call erode function to erode image
    erode_image = Erode(img)
    # call show function to show  original image and erode image
    Show(img, erode_image)


if __name__ == "__main__":
    main()

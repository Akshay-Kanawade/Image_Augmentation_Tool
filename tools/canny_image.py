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


def Canny(img, th1, th2):
    """
    This function is used for detecting edges by using canny edge detection method .
    :param th2: threshold value
    :param th1: threshold value
    :param img: ndarray
    :return: image
    """
    # use cv2.canny() function to detect edge in image
    # syntax : cv2.canny(src, threshold1, threshold2)
    return cv2.Canny(img, th1, th2)


def Show(orignal_img, canny_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param canny_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Canny_Image", canny_image)
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
    th1, th2 = map(int, input("enter th1, th2 value :").split(" "))
    # call canny function to detect edge on image
    canny_image = Canny(img, th1, th2)
    # call show function to show  original image and edge detected image
    Show(img, canny_image)


if __name__ == "__main__":
    main()

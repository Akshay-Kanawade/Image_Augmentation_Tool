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
    return cv2.imread(image_path, 0)


def Sobel(img):
    """
    This function is used for detecting edges by using sobel method in images.
    :param img: ndarray
    :return: image
    """
    # use cv2.sobel() function to detect edge in image
    # syntax : cv2.sobel(src, depth, dx, dy, ksize)
    return cv2.Sobel(img, cv2.CV_16U, 1, 0, ksize=5)


def Show(orignal_img, sobel_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param sobel_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Sobel_Image", sobel_image)
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
    # call sobel function to detect edge on image
    sobel_image = Sobel(img)
    # call show function to show  original image and edge detected image
    Show(img, sobel_image)


if __name__ == "__main__":
    main()

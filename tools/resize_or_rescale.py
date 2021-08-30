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


def Resize(img, h, w):
    """
    This function is used to resize the image as per the given height and width.
    :param img: ndarray
    :param h: height of image
    :param w: width of image
    :return: resized image
    """
    # use cv2.resize() function to resize image
    # cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
    return cv2.resize(img, (w, h))


def Show(img, resized_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param img: ndarray
    :param resized_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", img)
    cv2.imshow("Resized_Image", resized_image)
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
    # give height and width for resize image
    h, w = map(int, input("Enter height, width sep by space:").split(" "))
    # call resized function to resize image
    resized_image = Resize(img, h, w)
    # call show function to show  original image and resized image
    Show(img, resized_image)


if __name__ == "__main__":
    main()

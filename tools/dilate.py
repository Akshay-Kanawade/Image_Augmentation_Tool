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


def Dilate(img):
    """
    dilate is used to add pixel on object boundaries.
    :param img: ndarray
    :return: dilated image
    """
    # use cv2.dilate() function to flip image
    # syntax : cv2.dilate(src, kernel, iterations)
    return cv2.dilate(img, (7, 7), iterations=7)


def Show(orignal_img, dilate_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param dilate_image: ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Dilate_Image", dilate_image)
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
    # call dilate function to dilate image
    dilate_image = Dilate(img)
    # call show function to show  original image and dilate image
    Show(img, dilate_image)


if __name__ == "__main__":
    main()

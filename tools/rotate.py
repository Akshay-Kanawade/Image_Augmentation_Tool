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


def Rotate(img, deg):
    """
    this function is used for rotate the image as per specified degree.
    :param img: ndarray
    :param deg: angle
    :return: rotated image
    """
    # use cv2.getRotationMatrix2D() function to rotate the matrix as per input
    # syntax : cv2.wrapAffine(src, m, dsize )
    rows, cols, c = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), deg, 1)
    return cv2.warpAffine(img, M, (cols, rows))


def Show(orignal_img, rotated_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param rotated_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Rotated_Image", rotated_image)
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
    # give angle
    deg = int(input("enter the angle which we have to rotate image:"))
    # call rotate function used to rotate image as per angle
    rotated_image = Rotate(img, deg)
    # call show function to show  original image and rotated image
    Show(img, rotated_image)


if __name__ == "__main__":
    main()

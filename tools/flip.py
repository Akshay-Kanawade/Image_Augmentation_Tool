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


def Flip(img, direction):
    """
    Flip the image as per the direction if
    dir = 1 for vertically
    dir = 0 for horizontally
    dir = -1 for both horizontally and vertically
    :param img: ndarray
    :param direction: direction for which we have to flip
    :return: flip image
    """
    # use cv2.flip() function to flip image
    # syntax : cv2.flip(src, flipCode, dst)
    return cv2.flip(img, int(direction))


def Show(orignal_img, flip_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param flip_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Flip_Image", flip_image)
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
    # dir to which we have to flip input image
    direction = int(input("Enter 0 for horizontal ,1 for vertical, -1 for horizontal & vertical :"))
    # call flip function to flip image
    flip_image = Flip(img, direction)
    # call show function to show  original image and resized image
    Show(img, flip_image)


if __name__ == "__main__":
    main()

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


def Split(img):
    """
    This function is used for split image in red, green, blue channel.
    :param img: ndarray
    :return: image
    """
    # use cv2.split() function to split image
    # syntax : cv2.split(src, depth, dx, dy, ksize)
    b, g, r = cv2.split(img)
    return r, g, b


def Show(orignal_img, r, g, b):
    """
    show the images
    :param orignal_img: orignal input image
    :param r: red channel
    :param g: green channel
    :param b: blue channel
    :return: images
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("red_channel", r)
    cv2.imshow("green_channel", g)
    cv2.imshow("blue_channel", b)
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
    # call split function to split image
    r, g, b = Split(img)
    # call show function to show  original image and split image
    Show(img, r, g, b)


if __name__ == "__main__":
    main()

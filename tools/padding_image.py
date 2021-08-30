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


def Padding(img, x1, x2, y1, y2, color_value=None):
    """
    Add padding to input images
    :param img: ndarray
    :param x1: leftBorder
    :param x2: rightBorder
    :param y1: topBorder
    :param y2: bottomBorder
    :param color_value: color of border
    :return: padding image
    """
    # use cv2.copyMakeBorder() to add padding on images
    # cv2.copyMakeBorder(image, topBorder, bottomBorder, leftBorder, rightBorder, cv2.BORDER_CONSTANT,
    # value=color_of_border)
    if color_value is None:
        color_value = [0, 0, 0]
    return cv2.copyMakeBorder(img, y1, y2, x1,
                              x2, cv2.BORDER_CONSTANT, value=color_value)


def Show(orignal_img, paded_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param paded_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("paded_Image", paded_image)
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
    # give input (y1,y2,x1,x2)(bottom,top,left,right)
    x1, x2, y1, y2 = map(int, input("Enter left, right, bottom, top sep by space:").split(" "))
    color = tuple(map(int, input("Enter color of border sep by ',':").split(",")))
    # call padding function to add padding to image
    paded_image = Padding(img, x1, x2, y1, y2, color)
    # call show function to show  original image and resized image
    Show(img, paded_image)


if __name__ == "__main__":
    main()

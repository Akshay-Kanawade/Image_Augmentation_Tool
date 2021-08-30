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


def Brightness(img, contrast):
    """
    This function is used to increase the brightness of image .
    :param img: ndarray
    :param contrast: int
    :return: image
    """
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    image[:, :, 2] = [[max(pixel - contrast, 0) if pixel < 175 else min(pixel + contrast, 255) for pixel in row] for row
                      in image[:, :, 2]]
    return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)


def Show(orignal_img, brightness_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param brightness_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Bright_Image", brightness_image)
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
    # get value
    contrast = int(input("Enter the contrast value : "))
    # callBrightness() function to increase brightness of image
    bright_image = Brightness(img, contrast)
    # call show function to show  original image and bright image
    Show(img, bright_image)


if __name__ == "__main__":
    main()

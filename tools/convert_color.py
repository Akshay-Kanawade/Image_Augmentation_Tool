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


def Convert_color(img, code):
    """
    erode is used to remove pixel on object boundaries.
    :param img: ndarray
    :param code: color code
    :return: converted image
    """
    if code == "BGR2RGB":
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if code == "BGR2GRAY":
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if code == "BGR2HSV":
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if code == "BGR2HLS":
        return cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    if code == "RGB2GRAY":
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if code == "RGB2LAB":
        return cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    if code == "RGB2HSV":
        return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    if code == "GRAY2BGR":
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    if code == "GRAY2RGB":
        return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    if code == "LAB2RGB":
        return cv2.cvtColor(img, cv2.COLOR_LAB2RGB)
    if code == "LAB2BGR":
        return cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
    if code == "HSV2BGR":
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    if code == "HSV2RGB":
        return cv2.cvtColor(img, cv2.COLOR_HSV2RGB)


def Show(orignal_img, converted_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param converted_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Erode_Image", converted_image)
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
    # give code
    code = input("Enter the code (BGR2-> GRAY,RGB,HSV,LAB , RGB2->GRAY,LAB,HSV , HSV2->BGR,RGB , LAB2-> BGR,RGB):")
    # call CONVERT_COLOR function to convert the color of image image
    converted_image = Convert_color(img, code)
    # call show function to show  original image and color converted image
    Show(img, converted_image)


if __name__ == "__main__":
    main()

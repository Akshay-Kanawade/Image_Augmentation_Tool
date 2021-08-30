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


def Threshold(img, types):
    """
    This function is used to blur the image as per the given method.
    :param img: ndarray
    :param types: the method which we have to apply for thresholding the image.
              i.e THRESH_MASK, THRESH_BINARY, THRESH_TRUNC, THRESH_OTSU, THRESH_TOZERO,
              ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_TRIANGLE, THRESH_TOZERO_INV, THRESH_BINARY_INV
    :return: blur image
    """
    # use cv2.threshold() to blur the image
    # syntax : cv2.threshold(src, thresh, maxvalue, Type)

    if types == "THRESH_MASK":
        _, th = cv2.threshold(img, 255, 255, cv2.THRESH_MASK)
        return th
    if types == "THRESH_BINARY":
        _, th = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
        return th
    if types == "THRESH_BINARY_INV":
        _, th = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY_INV)
        return th
    if types == "THRESH_TRUNC":
        _, th = cv2.threshold(img, 155, 250, cv2.THRESH_TRUNC)
        return th
    if types == "THRESH_TRIANGLE":
        _, th = cv2.threshold(img, 125, 255, cv2.THRESH_TRIANGLE)
        return th
    if types == "THRESH_OTSU":
        _, th = cv2.threshold(img, 125, 255, cv2.THRESH_OTSU)
        return th
    if types == "THRESH_TOZERO":
        _, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
        return th
    if types == "THRESH_TOZERO_INV":
        _, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
        return th
    if types == "ADAPTIVE_THRESH_GAUSSIAN_C":
        _, th = cv2.threshold(img, 175, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        return th


def Show(orignal_img, threshold_Image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param threshold_Image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("threshold_Image", threshold_Image)
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
    # type which we have to apply for blur the image
    types = input("Enter the type (THRESH_MASK, THRESH_BINARY, THRESH_TRUNC, THRESH_OTSU, THRESH_TOZERO,"
              "ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_TRIANGLE, THRESH_TOZERO_INV, THRESH_BINARY_INV) : ")
    # call flip function to flip image
    threshold_image = Threshold(img, types)
    # call show function to show  original image and resized image
    Show(img, threshold_image)


if __name__ == "__main__":
    main()

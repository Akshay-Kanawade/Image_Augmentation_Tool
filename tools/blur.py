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


def Blur(img, types):
    """
    This function is used to blur the image as per the given method.
    :param img: ndarray
    :param types: the method which we have to apply for blur the image.
              i.e GaussianBlur, Averaging_blur, bilateralFilter, medianBlur.
    :return: blur image
    """
    if types == "Averaging_blur":
        # use cv2.blur() to blur the image
        # syntax : cv2.blur(src, ksize, dst, anchor, borderType)
        return cv2.blur(img, (9, 9))
    if types == "GaussianBlur":
        # use cv2.GaussianBlur() to blur the image
        # syntax : cv2.GaussianBlur(src, ksize, sigmx, dst, sigmay, bordertype)
        return cv2.GaussianBlur(img, (7, 7), 0.50)
    if types == "medianBlur":
        # use cv2.medianBlur() to blur the image
        # syntax : cv2.medianBlur(src, ksize,dst)
        return cv2.medianBlur(img, 9)
    if types == "bilateralFilter":
        # use cv2.bilateralFilter() to blur the image
        # syntax : cv2.bilateralFilter(src,  d, sigmaColor,sigmaSpace)
        return cv2.bilateralFilter(img, 9, 175, 175)


def Show(orignal_img, blur_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param blur_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Blur_Image", blur_image)
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
    types = input("Enter the type (GaussianBlur, Averaging_blur, bilateralFilter, medianBlur) : ")
    # call flip function to flip image
    blur_image = Blur(img, types)
    # call show function to show  original image and resized image
    Show(img, blur_image)


if __name__ == "__main__":
    main()

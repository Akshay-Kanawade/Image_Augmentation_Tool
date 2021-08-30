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


def Interplotate(img, types):
    """
    This function is used to interpolate the image as per the given interpolate method.
    :param img: ndarray
    :param types: the method which we have to apply for interplotation of image.
              i.e INTER_NEAREST, INTER_LINEAR, INTER_CUBIC
    :return: interplotate image
    """
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    angle45 = 45
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angle45, scale)

    abs_cos = abs(M[0, 0])
    abs_sin = abs(M[0, 1])

    bound_w = int(h * abs_sin + w * abs_cos)
    bound_h = int(h * abs_cos + w * abs_sin)

    M[0, 2] += bound_w / 2 - center[0]
    M[1, 2] += bound_h / 2 - center[1]

    rotated30 = cv2.warpAffine(img, M, (bound_w, bound_h))

    scale_percent = 110
    width = int(rotated30.shape[1] * scale_percent / 100)
    height = int(rotated30.shape[0] * scale_percent / 100)
    dim = (width, height)

    if types == "INTER_NEAREST":
        return cv2.resize(rotated30, dim, interpolation=cv2.INTER_NEAREST)
    if types == "INTER_LINEAR":
        return cv2.resize(rotated30, dim, interpolation=cv2.INTER_LINEAR)
    if types == "INTER_CUBIC":
        return cv2.resize(rotated30, dim, interpolation=cv2.INTER_CUBIC)


def Show(orignal_img, interplotate_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param interplotate_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Interplotate_Image", interplotate_image)
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
    types = input("Enter the type (INTER_NEAREST, INTER_LINEAR, INTER_CUBIC) : ")
    # call interplotate function to interplotate image
    interplotate_image = Interplotate(img, types)
    # call show function to show  original image and interplotate image
    Show(img, interplotate_image)


if __name__ == "__main__":
    main()

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


def Crop(img, x1, x2, y1, y2):
    """
    crop the image as per given inputs.
    :param img: ndarray
    :param x1: left
    :param x2: right
    :param y1: bottom
    :param y2: top
    :return: cropped image
    """
    # (y1,y2,x1,x2)(bottom,top,left,right)
    h, w = img.shape[1], img.shape[0]
    return img[x1:h-x2, y1:w-y2]


def Show(orignal_img, croped_image):
    """
    The show function gives the input as in the form of ndarray and show the image as output.
    :param orignal_img: ndarray
    :param croped_image:  ndarray
    :return: show image as output
    """
    # use imshow() function to show the images
    # syntax : cv2.imshow(winname, mat)
    cv2.imshow("Original_Image", orignal_img)
    cv2.imshow("Croped_Image", croped_image)
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
    # call crop function to crop image
    croped_image = Crop(img, x1, x2, y1, y2)
    # call show function to show  original image and resized image
    Show(img, croped_image)


if __name__ == "__main__":
    main()

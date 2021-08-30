import os
import cv2

from tools.Show_image import Show
from tools.blur import Blur
from tools.brightness import Brightness
from tools.canny_image import Canny
from tools.convert_color import Convert_color
from tools.crop import Crop
from tools.invert import Invert
from tools.dilate import Dilate
from tools.emboss_image import Emboss
from tools.erode import Erode
from tools.flip import Flip
from tools.interplotation import Interplotate
from tools.negative import Negative
from tools.noise import Noise
from tools.normalize import Normalize
from tools.padding_image import Padding
from tools.resize_or_rescale import Resize
from tools.rotate import Rotate
from tools.sharpen_image import Sharp
from tools.sobel_image import Sobel
from tools.split_image import Split
from tools.threshold import Threshold
from tools.translation import Translate


def Read(img_path):
    """
    This function basically used to read the image.It read images in form of numpy array.
    :param img_path: source image
    :return: ndarray
    """
    # use cv2.imread()  to read an images.
    # syntax : cv2.imread(filename, flag=None)
    return cv2.imread(img_path)


def main(operation, src, target):
    """
    This is a main function.
    :param operation: the operations which we have to perform
    :param src:  source folder
    :param target: target folder
    :return: nothing
    """

    images = os.listdir(src)
    print(images)
    # iterate through the image list
    for file in images:
        # get file name
        filename = file.split('.')[0]
        # read image
        img = Read(f"{src}/{file}")
        if operation == "Show":
            # call show function to show image
            Show(img)
        if operation == "Invert":
            # call show function to show image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Invert(img))
        if operation == "Blur":
            # type which we have to apply for blur the image
            types = input("Enter the type (GaussianBlur, Averaging_blur, bilateralFilter, medianBlur) : ")
            # call blur function to blur image
            cv2.imwrite(f"{target}/{types + '_' + filename}.jpg", Blur(img, types))
        if operation == "Brightness":
            # get value
            contrast = int(input("Enter the contrast value : "))
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Brightness(img, contrast))
        if operation == "Canny":
            # give threshold value
            th1, th2 = map(float, input("enter th1, th2 value :").split(" "))
            # call canny function to detect edge on image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Canny(img, th1, th2))
        if operation == "Convert_color":
            # give code
            code = input(
                "Enter the code (BGR2-> GRAY,RGB,HSV,LAB , RGB2->GRAY,LAB,HSV , HSV2->BGR,RGB , LAB2-> BGR,RGB):")
            # call CONVERT_COLOR function to convert the color of image image
            cv2.imwrite(f"{target}/{'color'+code + '_' + filename}.jpg", Convert_color(img, code))
        if operation == "Crop":
            # give input (y1,y2,x1,x2)(bottom,top,left,right)
            x1, x2, y1, y2 = map(int, input("Enter left, right, bottom, top sep by space:").split(" "))
            # call crop function to crop image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Crop(img, x1, x2, y1, y2))
        if operation == "Dilate":
            # call dilate function to dilate image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Dilate(img))
        if operation == "Emboss":
            # call emboss function to emboss image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Emboss(img))
        if operation == "Erode":
            # call erode function to erode image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Erode(img))
        if operation == "Flip":
            # dir to which we have to flip input image
            direction = input("Enter 0 for horizontal ,1 for vertical, -1 for horizontal & vertical :")
            # call flip function to flip image
            cv2.imwrite(f"{target}/{operation + '_'+ direction +'_'+ filename}.jpg", Flip(img, direction))
        if operation == "Interplotate":
            types = input("Enter the type (INTER_NEAREST, INTER_LINEAR, INTER_CUBIC) : ")
            # call interplotate function to interplotate image
            cv2.imwrite(f"{target}/{ operation+ '_'+types+'_' + filename}.jpg", Interplotate(img, types))
        if operation == "Negative":
            # call negative function to invert image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Negative(img))
        if operation == "Noise":
            # call Noise() function to add noise on image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Noise(img))
        if operation == "Normalize":
            # call normalize function to normalize image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Normalize(img))
        if operation == "Padding":
            # give input (y1,y2,x1,x2)(bottom,top,left,right)
            x1, x2, y1, y2 = map(int, input("Enter left, right, bottom, top sep by space:").split(" "))
            color = tuple(map(int, input("Enter color of border sep by ',':").split(",")))
            # call padding function to add padding to image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Padding(img, x1, x2, y1, y2, color))
        if operation == "Resize":
            # give height and width for resize image
            h, w = map(int, input("Enter height, width sep by space:").split(" "))
            # call resized function to resize image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Resize(img, h, w))
        if operation == "Rotate":
            # give angle
            deg = int(input("enter the angle which we have to rotate image:"))
            # call rotate function used to rotate image as per angle
            cv2.imwrite(f"{target}/{operation + '_'+ str(deg)+'_' + filename}.jpg", Rotate(img, deg))
        if operation == "Sharp":
            # call flip function to sharp the image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Sharp(img))
        if operation == "Sobel":
            # call sobel function to detect edge on image
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Sobel(img))
        if operation == "Split":
            # call split function to split image
            r, g, b = Split(img)
            cv2.imwrite(f"{target}/{operation + '_' + 'g'+ filename}.jpg", g)
            cv2.imwrite(f"{target}/{operation + '_' + 'b'+ filename}.jpg", b)
            cv2.imwrite(f"{target}/{operation + '_' +'r'+ filename}.jpg", r)
        if operation == "Threshold":
            # type which we have to apply for blur the image
            types = input("Enter the type (THRESH_MASK, THRESH_BINARY, THRESH_TRUNC, THRESH_OTSU, THRESH_TOZERO,"
                              "ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_TRIANGLE, THRESH_TOZERO_INV, THRESH_BINARY_INV) : ")
            # call flip function to flip image
            cv2.imwrite(f"{target}/{operation + '_'+ types+'_' + filename}.jpg", Threshold(img, types))
        if operation == "Translate":
            # give threshold value
            x, y = map(int,
                           input("enter value -x -> left, -y -> up, x -> right, y -> down  for translation:")
                           .split(" "))
            # call translate function to translate image in x and y direction
            cv2.imwrite(f"{target}/{operation + '_' + filename}.jpg", Translate(img, x, y))


if __name__ == "__main__":
    aug = input("Enter the operations:")
    src_path = "source"
    target_path = "target"
    main(aug, src_path, target_path)

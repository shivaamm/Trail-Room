# Image basic adjustment: image brightness, contrast, chroma, can also be used to enhance image sharpness, whitening
# """

from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np


# image = Image.open('14.jpg')
#image.show()
def BrightnessEnhancement(brightness):
    # '''
    #  #Brightness enhancement: brightness is between (0-1), the new image is darker than the original image, and the new image is brighter than the original image at (1-~),
    #  ##brightness=1, keep the original image unchanged; the parameter range can be customized
    # '''
    image = Image.open(filepath)
    enh_bri = ImageEnhance.Brightness(image)
#    brightness =1.5
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()

def ContrastEnhancement(contrast):
    # '''
    #  #Contrast enhancement: customizable parameter contrast range, contrast=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_con = ImageEnhance.Contrast(image)
#    contrast =1.5
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()

def ColorEnhancement(color):
    # '''
    #  #Chroma enhancement: saturation color=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_col = ImageEnhance.Color(image)
#    color =0.8
    image_colored = enh_col.enhance(color)
    image_colored.show()

def SharpnessEnhancement(sharpness):
    # '''
    #  #Sharpness enhancement: sharpness sharpness=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_sha = ImageEnhance.Sharpness(image)
#    sharpness = 2
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()

def Filter(image):
    # """
    #  The radius of the color window
    #  The image will show a similar effect to microdermabrasion
    # """
    #image: input image, can be Mat type,
    #              The image must be an 8-bit or floating-point single-channel or three-channel image
    #0: indicates the diameter range of each pixel neighborhood in the filtering process, generally 0
    #The last two numbers: standard deviation of spatial Gaussian function, standard deviation of gray value similarity
    image =cv2.imread(filepath)
    Remove=cv2.bilateralFilter(image,0,0,10)
    cv2.imshow('filter',Remove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#    res = np.uint8(np.clip((1.2 * image + 10), 0, 255))
#    tmp = np.hstack((dst, res))
#    cv2.imshow('bai',res)


def WhiteBeauty(image,whi):
    # '''
    #  Whitening
    # '''
    import cv2

    image =cv2.imread(filepath)
    white = np.uint8(np.clip((whi * image + 10), 0, 255))
    cv2.imshow('bai',white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ =="__main__":
    filepath = 'D:\PHOTOS\choki dhani\Mayank Chittora.PNG'
    #The original image
    brightness = 1.5
    contrast = 0.2
    color=1.9
    sharpness=0.1
    BrightnessEnhancement(brightness)
    ContrastEnhancement(contrast)
    ColorEnhancement(color)
    SharpnessEnhancement(sharpness)
    whi = 1.2
    image =cv2.imread('D:\PHOTOS\choki dhani\Mayank Chittora.PNG')
    Filter(image)
    WhiteBeauty(image,whi)
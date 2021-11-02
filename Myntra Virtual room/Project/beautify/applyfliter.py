# Image basic adjustment: image brightness, contrast, chroma, can also be used to enhance image sharpness, whitening
# """

from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np




from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


# image = Image.open('14.jpg')
#image.show()
def BrightnessEnhancement(brightness,filepath):
    # '''
    #  #Brightness enhancement: brightness is between (0-1), the new image is darker than the original image, and the new image is brighter than the original image at (1-~),
    #  ##brightness=1, keep the original image unchanged; the parameter range can be customized
    # '''
    image = Image.open(filepath)
    enh_bri = ImageEnhance.Brightness(image)
#    brightness =1.5
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()

def ContrastEnhancement(contrast,filepath):
    # '''
    #  #Contrast enhancement: customizable parameter contrast range, contrast=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_con = ImageEnhance.Contrast(image)
#    contrast =1.5
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()

def ColorEnhancement(color,filepath):
    # '''
    #  #Chroma enhancement: saturation color=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_col = ImageEnhance.Color(image)
#    color =0.8
    image_colored = enh_col.enhance(color)
    image_colored.show()

def SharpnessEnhancement(sharpness,filepath):
    # '''
    #  #Sharpness enhancement: sharpness sharpness=1, keep the original image unchanged
    # '''
    image = Image.open(filepath)
    enh_sha = ImageEnhance.Sharpness(image)
#    sharpness = 2
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()

def Filter(image,filepath):
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


def WhiteBeauty(image,whi,filepath):
    # '''
    #  Whitening
    # '''
    import cv2
    image =cv2.imread(filepath)
    white = np.uint8(np.clip((whi * image + 10), 0, 255))
    cv2.imshow('bai',white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def def_apply(filepath):
    #The original image
    brightness = 1.5
    contrast = 0.2
    color=1.9
    sharpness=0.1
    BrightnessEnhancement(brightness,filepath)
    # ContrastEnhancement(contrast,filepath)
    # ColorEnhancement(color,filepath)
    # SharpnessEnhancement(sharpness,filepath)
    whi = 1.2
    image =cv2.imread(filepath)
    Filter(image,filepath)
    # WhiteBeauty(image,whi,filepath)



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.maxsize(200, 300)

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        # self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        filepath  = self.filename
        def_apply(filepath)



def main_fun():
    root = Root()
    root.geometry("500x200")
    root.mainloop()


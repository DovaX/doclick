from PIL import ImageGrab
from PIL import Image, ImageDraw

def take_screenshot():
    img = ImageGrab.grab()
    return(img)

def load_img(path):
    img=Image.open(path)
    return(img)

def get_pixel(img,x,y):
    pix=img.load()
    return(pix[x,y])

def save_img(img,filename):
    img.save(filename)
    




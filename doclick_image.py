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
    



def project_rgb(inp,rgb=0):
    "rgb parameter ... 0 ~ R, 1 ~ G, 2 ~ B"
    if isinstance(inp,tuple):
        return(inp[0])
    if isinstance(inp,list):
        return([x[0] for x in inp])
        
    
def get_col_pixels(pix,x,y_size):
    col_pixels=[pix[x,i] for i in range(y_size)]
    return(col_pixels)
    


def get_pattern(subimg,subimg_x):
    subpix=subimg.load()
    sub_y_size=subimg.size[1]
    column=get_col_pixels(subpix,subimg_x,sub_y_size)
    red_column=project_rgb(column)
    pattern=str(red_column)[1:-1]    
    return(pattern)

def get_template(img):

    pix=img.load()
    y_size=img.size[1]
    all_pixels_data=[]
    for x in range(img.size[0]):
        column=get_col_pixels(pix,x,y_size)
        red_template_col=project_rgb(column)
        all_pixels_data.append(red_template_col)
    return(all_pixels_data)



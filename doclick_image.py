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


    
def get_matching_columns(all_pixels_data,size_x,subimg,subimg_x,threshold=100):
    #Threshold ~ max number of subimg occurences
    pattern=get_pattern(subimg,subimg_x)    
    
    matching_cols=[] 
    
    for x in range(size_x):
        red_template_col=all_pixels_data[x]
        if pattern in str(red_template_col):
            first_part=str(red_template_col).split(pattern)[0]
            y=first_part.count(",")
            matching_cols.append([x,y])
    if len(matching_cols)>threshold:
        return([])
    else:
        print("Pattern found in coordinates:",matching_cols)
    return(matching_cols)


def get_division(subimg,division_points=20):
    subimg_size_x=subimg.size[0]
    
    if division_points==0:
        division=list(range(subimg_size_x))
    else:
        division=list(range(0,subimg_size_x,subimg_size_x//division_points))   
    return(division)        


def detect_subimg(img,subimg,division_points=20):
    #compares only one colour
    division=get_division(subimg,division_points)
    basis_points_dict={}
    counter=0
    all_pixels_data=get_template(img)
    
    for i in range(len(division)):
        matching_cols=get_matching_columns(all_pixels_data,img.size[0],subimg,division[i])
        basis_points=[(coor[0]-division[i],coor[1]) for coor in matching_cols]
        
        for point in basis_points:
            if point in basis_points_dict.keys():
                basis_points_dict[point]+=1
            else:
                basis_points_dict[point]=1
        if len(matching_cols)>0:
            counter+=1
    
    true_points=[]
    for k,v in basis_points_dict.items():
        if v==counter and counter>division_points//10 and counter>1:
            true_points.append(k)
    
    return(true_points)
            

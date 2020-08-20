import pynput.mouse
import pynput.keyboard
import time
import datetime
import doclick_image


mouse = pynput.mouse.Controller()
button = pynput.mouse.Button
keyboard = pynput.keyboard.Controller()
key = pynput.keyboard.Key


class Clicker:
    def __init__(self):
        pass
    
    def move(self,width,height):
        mouse.position=[width,height]
        
    def relative_move(self,width,height):
        """not implemented from pseudolanguage"""
        mouse.move(width,height)
        
    def click(self,width,height):
        self.move(width,height)
        mouse.click(button.left,1)

    def write(self,text):
        if text=="%{TAB}":
            with keyboard.pressed(key.alt):
                keyboard.press(key.tab)
                keyboard.release(key.tab)
        elif text=="%{TAB 2}":
            with keyboard.pressed(key.alt):
                keyboard.press(key.tab)
                keyboard.release(key.tab)
                time.sleep(0.1)
                keyboard.press(key.tab)
                keyboard.release(key.tab)
        elif text=="%{TAB 3}":
            with keyboard.pressed(key.alt):
                keyboard.press(key.tab)
                keyboard.release(key.tab)
                time.sleep(0.1)
                keyboard.press(key.tab)
                keyboard.release(key.tab)
                time.sleep(0.1)
                keyboard.press(key.tab)
                keyboard.release(key.tab)
        elif text=="%T":
            with keyboard.pressed(key.alt):
                keyboard.type("T")
                
        elif text=="{DOWN}":
            keyboard.press(key.down)
            keyboard.release(key.down)

        elif text=="{ESC}":
            keyboard.press(key.esc)
            keyboard.release(key.esc)
                
        elif text=="{F5}":
            #with keyboard.pressed(key.alt):
            keyboard.press(key.f5)
            keyboard.release(key.f5)
        elif text=="{ENTER}":
            #with keyboard.pressed(key.alt):
            keyboard.press(key.enter)
            keyboard.release(key.enter)
         
            
            
        else:
            keyboard.type(text)
            
            
    def write_time(self):
        now=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.write(now)
        
    def press(self,key='shift'):
        """not implemented from pseudolanguage"""
        if key=='ctrl':
            keyboard.press(key.ctrl)
        elif key=='alt':
            keyboard.press(key.alt)
        elif key=='shift':
            keyboard.press(key.shift)
            
    def condition_subimage(self,sub_img):      
            
        main_img=doclick_image.take_screenshot()
        detected_img_coor_list=doclick_image.detect_subimg(main_img,sub_img)
        if len(detected_img_coor_list)>0:
            print(detected_img_coor_list)
            return(True)
        else:
            return(False)
        
    def condition_day_time(self,opening_time,closing_time):
        """Enable scheduling of work only in day time
        inputs: opening time and closing time in hours (int)"""
        hours=int(datetime.datetime.now().strftime("%H"))
        if hours>=opening_time and hours<closing_time:
            return(True)
        else:
            return(False)
        
    def wait_until_satisfied_day_time(self):
        done = False
        while not done:
            time.sleep(30)
            if self.condition_day_time(5,22):
                done=True
                print("done=True")
            else:
                print("Script not active")
        
        
    def wait_until_satisfied(self,sub_img_path):
        done = False
        
        while not done:
            #print("A")
            img=doclick_image.load_img(sub_img_path)
            #print(self.condition_subimage(img)) 
            if self.condition_subimage(img):
                done=True
                print("done=True")
        
    def wait_until_not_satisfied(self,sub_img_path):
        done = False
        
        while not done:
            print("B")
            img=doclick_image.load_img(sub_img_path)
            
            if not self.condition_subimage(img):
                done=True
                print("done=True")

    def wait(self,milliseconds):
        time.sleep(milliseconds/1000)
        
c=Clicker()


"""Reads orders in script.txt and executes them"""


def execute_script(script):
    with open(script,"r") as file:
        lines = file.readlines()
        orders = [x.replace("\n","") for x in lines]
    
    for i,order in enumerate(orders):
        execute_order(order)
            


def execute_order(order):
    if "Click" in order:
        position=order[:-1].replace("Click(","").split(",")
        c.click(position[0],position[1])
        
    elif "Wait" in order:
        milliseconds=int(order[:-1].replace("Wait(",""))
        c.wait(milliseconds)
        
    elif "WriteTime" in order:
        c.write_time()
        
    elif "Write" in order:
        text=order[:-1].replace("Write(","")
        c.write(text)  
        
    elif "Call" in order:
        script=order[:-1].replace("Call(","")        
        execute_script(script)
        
    ###### IMAGE #######
    elif "Screenshot" in order:
        img=doclick_image.take_screenshot()
        doclick_image.save_img(img,"screenshot.png") 
        
    elif "GetPixel" in order:
        img=doclick_image.load_img("screenshot.png") 
        x,y=(200,200)
        pixel=doclick_image.get_pixel(img,x,y)
        print(pixel)
        
    elif "RepeatInDayTime" in order:
        c.wait_until_satisfied_day_time()
    
    elif "RepeatUntilSubimage" in order:
        path=order[:-1].replace("RepeatUntilSubimage(","")
        c.wait_until_satisfied(path)
        
    elif "RepeatUntilNotSubimage" in order:
        path=order[:-1].replace("RepeatUntilNotSubimage(","")
        c.wait_until_not_satisfied(path)
    
    elif "Print" in order:
        text=order[:-1].replace("Print(","")
        print(text)
        
        
execute_script("script.txt")
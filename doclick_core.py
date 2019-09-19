import pynput.mouse
import pynput.keyboard
import time
import datetime


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
        elif text=="%{TAB 3}":
            with keyboard.pressed(key.alt):
                keyboard.press(key.tab)
                keyboard.release(key.tab)
                keyboard.press(key.tab)
                keyboard.release(key.tab)
                keyboard.press(key.tab)
                keyboard.release(key.tab)
        elif text=="%T":
            with keyboard.pressed(key.alt):
                keyboard.type("T")
                
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

execute_script("script.txt")
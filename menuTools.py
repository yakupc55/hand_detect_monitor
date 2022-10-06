from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import cv2
class menuItem():
    def __init__(self,no):
        self.no =no
        self.x= 0
        self.y = 0
        self.text =""
        self.w=0
        self.h=0
        self.bgColor=(0,0,0)
        self.textCords =[]

class TextCord():
    def __init__(self,x,y,text):
        self.x =x
        self.y =y
        self.text= text

class TextSettings():
    def __init__(self,betweenSpace,spaceWidth,textHeight):
        self.betweenSpace =betweenSpace
        self.spaceWidth =spaceWidth
        self.textHeight= textHeight

class textProcess():
    def __init__(self,no):
        self.no =no
    def writeTextUsingTurkishLibrary(self,text):
        print("test")

class _settings:
    information = True
    handShow = True
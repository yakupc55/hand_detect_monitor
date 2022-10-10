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
    handShow = False
    isFlipMode = True
    informationText ="None"
    fingerCode = -1
    fingerStringList = ""

class dataSender:
    imgData = []
    textList = []
    senderFinish =False

class textProcess:
    def putText(img,text,x,y):
        ##########
        ##yazı yazmak için gerekli paremetreler
        # font
        textFont = cv2.FONT_HERSHEY_SIMPLEX
        textOrg = (x, y)
        
        # fontScale
        fontScale = 1
        
        # Blue color in BGR
        textColor = (255, 0, 0)
        
        # Line thickness of 2 px
        textThickness = 2
        #######
        img = cv2.putText(img, text, textOrg, textFont, 
                   fontScale, textColor, textThickness, cv2.LINE_AA)
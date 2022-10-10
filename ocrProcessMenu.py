from cmath import nan
import cv2
import numpy as np
import menuTools as mt
import easyocr
import argparse

from threading import Thread 
import time

def ocrListShow(result):
    list =[]
    for res in result:
        list.append(res[1])
    return list

def _threadOcr():
    reader = easyocr.Reader(['en'])
    result = reader.readtext(mt.dataSender.imgData)
    # print(ocrListShow(result))
    # print("calışıyor")
    mt.dataSender.textList = ocrListShow(result)
    mt.dataSender.senderFinish = True

class OcrProcessMenu():

    def __init__(self,menu):
        self.menu = menu
        self.tabMenuRow = 0
        self.menuBackColor = (20,20,20)
        self.childMenuWidth = 200
        self.childMenuHeight = 80
        self.space= 4
        self.menuList = []
        self.maxMenuWidth=0
        self.maxMenuHeight = 0
        self.menuTextList = ["Ust Menu'ye Git"]
        self.menuCount = len(self.menuTextList)
        menu.calculateMenuList(self)
        self.fontScale = 1.0
        self.textFont = cv2.FONT_HERSHEY_SIMPLEX
        self.textColor = (0, 255, 255)
        self.textThickness = 2
        self.textHeightSpace = 8
        self.textInfo =mt.TextSettings(0,0,0)
        menu.calculateTextForMultiLine(self.childMenuWidth,self.childMenuHeight,self.menuTextList,self.fontScale,self.textFont,self.textColor,self.textThickness,self.textHeightSpace,self.menuList,self.textInfo)

        self.startControl= False
        self.ocrControl = False
        self.flipControl = True
        self.informationText =""
        self.extraInfo =""


    def firstOpen(self):
        self.informationText = "ocr modu bekleniyor"
        
        
        
    def fingerPress(self,key):
        if key == 1 and self.startControl:
            self.ocrProcess()
            self.startControl = False
        elif key == 8 and self.flipControl:
            self.changeFlipMode()
            self.flipControl = False
        elif key == 0:
            self.informationText = "ocr modu bekleniyor"
            self.startControl= True
            self.flipControl = True

    def changeFlipMode(self):
        print("flip moduna girildi")
        mt._settings.isFlipMode = not mt._settings.isFlipMode
        if mt._settings.isFlipMode:
            self.informationText = "ters ekran acik"
        else:
            self.informationText = "ters ekran kapali"

    def ocrController(self):
        if self.ocrControl:
            #print("start control is working in first if")
            if mt.dataSender.senderFinish:
                print(mt.dataSender.textList)
                self.ocrControl = False
                mt.dataSender.senderFinish=False

    def drawFirst(self):
        self.ocrController()
        mt._settings.informationText = self.informationText
        #print("its working")
        overlay = self.menu.img.copy()
        mt.textProcess.putText(overlay,self.informationText,50,650)

        alpha = 0.4  # Transparency factor.
        self.menu.drawMenus(overlay)
        # Following line overlays transparent rectangle over the image
        self.menu.overlay = cv2.addWeighted(overlay, alpha, self.menu.img, 1 - alpha, 0)

    def clickaMenu(self,menuCode):
        #print("menu code : "+str(menuCode))
        if menuCode == 0:
            self.goMainMenu()
        else:
            print("its not a menu code")
    
    

    def ocrProcess(self):
        print("OCR process is working")
        if not self.ocrControl:
            print("ocr if process is working")
            self.informationText = "ocr modu calistirildi"
            mt.dataSender.imgData = self.menu.img.copy()
            x = Thread(target=_threadOcr)
            x.start()
            self.ocrControl=True

    def goMainMenu(self):
        self.menu.changeCurrentMenu(0)

    def cleanup_text(self,text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	    return "".join([c if ord(c) < 128 else "" for c in text]).strip
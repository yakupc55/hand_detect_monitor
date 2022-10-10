import cv2
import numpy as np
import menuTools as mt
class emptyMenu():
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

    def firstOpen(self):
        print("ilk işlem çalışıyor")
        
    def fingerPress(self,key):
        print("working")

    def drawFirst(self):
        
        #print("its working")
        overlay = self.menu.img.copy()

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

    def goMainMenu(self):
        self.menu.changeCurrentMenu(0)
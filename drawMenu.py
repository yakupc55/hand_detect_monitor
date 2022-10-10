import cv2
import numpy as np
import menuTools as mt
class DrawMenu():
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
        self.menuTextList = ["Ust Menu'ye Git",
        "Yesil Renk",
        "Kirmizi Renk",
        "Mavi Renk",
        "Silgi Modu",
        "Hepsini Sil"]
        self.menuCount = len(self.menuTextList)
        menu.calculateMenuList(self)
        self.fontScale = 1.0
        self.textFont = cv2.FONT_HERSHEY_SIMPLEX
        self.textColor = (0, 255, 255)
        self.textThickness = 2
        self.textHeightSpace = 8
        self.textInfo =mt.TextSettings(0,0,0)
        menu.calculateTextForMultiLine(self.childMenuWidth,self.childMenuHeight,self.menuTextList,self.fontScale,self.textFont,self.textColor,self.textThickness,self.textHeightSpace,self.menuList,self.textInfo)
        self.currentColor = (0,255,0)
        self.drawArea = np.zeros((720,1280,3),np.uint8)
        self.xp = 0
        self.yp = 0
        self.brushThickness =  15
        self.eraserThickness = 100
        self.currentText= "Cizim rengi : Yesil"

    def firstOpen(self):
        print("ilk işlem çalışıyor")
        
    def drawOnScreen(self,overlay):
        alpha = 0.3
        return cv2.addWeighted(overlay,alpha,self.drawArea,1-alpha,0)

    def drawMode(self,x,y):
        self.controlPosition(x,y)
        if self.currentColor == (0,0,0):
            brush = self.eraserThickness
        else:
            brush = self.brushThickness
        cv2.line(self.menu.overlay,(self.xp,self.yp),(x,y),self.currentColor,brush)
        cv2.line(self.drawArea,(self.xp,self.yp),(x,y),self.currentColor,brush)
        self.xp = x
        self.yp = y

    def changeSomething(self):
        self.xp = 0
        self.yp = 0

    def controlPosition(self,x,y):
        if self.xp ==0 and self.yp == 0:
            self.xp=x
            self.yp=y

    def fingerPress(self,key):
        x, y = self.menu.getxyCordinat()
        if y>self.maxMenuHeight+30:
            #mt._settings.informationText="in area"
            if key == 2 or key ==6:
                self.drawMode(x,y)
            else:
                self.changeSomething()
        else:
            self.changeSomething()
            #mt._settings.informationText="not area"

    def drawFirst(self):
        #print("its working")
        mt._settings.informationText = self.currentText
        overlay = self.menu.img.copy()
        overlay = self.drawOnScreen(overlay)

        alpha = 0.6  # Transparency factor.
        self.menu.drawMenus(overlay)
        # Following line overlays transparent rectangle over the image
        self.menu.overlay = cv2.addWeighted(overlay, alpha, self.menu.img, 1 - alpha, 0)

    def clickaMenu(self,menuCode):
        #print("menu code : "+str(menuCode))
        if menuCode == 0:
            self.goMainMenu()
        elif menuCode == 1:
            self.changeColorToGreen()
        elif menuCode == 2:
            self.changeColorToRed()
        elif menuCode == 3:
            self.changeColorToBlue()
        elif menuCode == 4:
            self.clearMode()
        elif menuCode == 5:
            self.clearAllPage()
        else:
            print("its not a menu code")

    def goMainMenu(self):
        self.menu.changeCurrentMenu(0)

    def changeColorToGreen(self):
        self.currentText= "Cizim rengi : Yesil"
        self.currentColor = (0,255,0)

    def changeColorToRed(self):
        self.currentText= "Cizim rengi : Kirmizi"
        self.currentColor = (0,0,255)

    def changeColorToBlue(self):
        self.currentText= "Cizim rengi : Mavi"
        self.currentColor = (255,0,0)
    
    def clearMode(self):
        self.currentText= "Silgi Modu"
        self.currentColor = (0,0,0)
    
    def clearAllPage(self):
        self.drawArea = np.zeros((720,1280,3),np.uint8)
        self.currentText= "Hepsi silindi, Cizim rengi : Yesil"
        self.currentColor = (0,255,0)
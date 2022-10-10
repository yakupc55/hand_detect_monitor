import cv2
import menuTools as mt
class MainMenu():
    def __init__(self,menu):
        self.menu = menu
        self.tabMenuRow = 0
        self.menuBackColor = (255,123,123)
        self.childMenuWidth = 400
        self.childMenuHeight = 100
        self.space= 4
        self.menuList = []
        self.maxMenuWidth=0
        self.maxMenuHeight = 0
        self.menuTextList = ["Ayarlara Git",
        "Menu Testleri",
        "Cizim Yap",
        "Nesne Tanimla",
        "Test sistem 1"]
        self.menuCount = len(self.menuTextList)
        menu.calculateMenuList(self)
        self.fontScale = 1.4
        self.textFont = cv2.FONT_HERSHEY_SIMPLEX
        self.textColor = (0, 255, 255)
        self.textThickness = 2
        self.textHeightSpace = 8
        self.textInfo =mt.TextSettings(0,0,0)
        menu.calculateTextForMultiLine(self.childMenuWidth,self.childMenuHeight,self.menuTextList,self.fontScale,self.textFont,self.textColor,self.textThickness,self.textHeightSpace,self.menuList,self.textInfo)

    def fingerPress(self,key):
        
        if key == 4:
            print("a test")
            #self.menu.changeCurrentMenu(1)

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
            self.goSettingsMenu()
        elif menuCode == 1:
            self.goMenuTestMenu()
        elif menuCode == 2:
            self.goDrawMenu()
        elif menuCode == 3:
            self.goDetectObjectMenu()
        elif menuCode == 4:
            self.gotestProcessMenu()
        else:
            print("its not a menu code")

    
    def goSettingsMenu(self):
        self.menu.changeCurrentMenu(1)
    
    def goMenuTestMenu(self):
        self.menu.changeCurrentMenu(2)
    
    def goDrawMenu(self):
        self.menu.changeCurrentMenu(3)
    
    def goDetectObjectMenu(self):
        self.menu.changeCurrentMenu(4)
    
    def gotestProcessMenu(self):
        self.menu.changeCurrentMenu(5)

    
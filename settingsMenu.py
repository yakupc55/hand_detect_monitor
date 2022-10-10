import cv2
import menuTools as mt
class SettingsMenu():
    def __init__(self,menu):
        self.menu = menu
        self.tabMenuRow = 0
        self.menuBackColor = (20,20,20)
        
        self.childMenuWidth = 300
        self.childMenuHeight = 100
        self.space= 4
        self.menuList = []
        self.maxMenuWidth=0
        self.maxMenuHeight = 0
        self.menuTextList = ["Ust Menu'ye Git",
        "",
        "",
        ""]
        self.menuCount = len(self.menuTextList)
        menu.calculateMenuList(self)
        self.fontScale = 1.2
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
    def firstOpen(self):
        self.changeHandShowText()
        self.changeInformationShowText()
        self.changeFlipModeShowText()
        
    def drawFirst(self):
        mt._settings.informationText = " parmaklar :"+mt._settings.fingerStringList + " , Parmak Kodu :"+str(mt._settings.fingerCode)
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
        elif menuCode == 1:
            self.changeHandShow()
        elif menuCode == 2:
            self.changeInformationShow()
        elif menuCode == 3:
            self.changeFlipModeShow()
        else:
            print("its not a menu code")

    def goMainMenu(self):
        self.menu.changeCurrentMenu(0)

    def changeShowText(self,control,code,text1,text2):
        if control:
            newText = text1
        else:
            newText = text2
        self.menuList[code].text = newText
        self.menuList[code].textCords = self.menu.calculateMenuTextForaItem(newText)

    def changeHandShowText(self):
        self.changeShowText(mt._settings.handShow,1,"El Hareketlerini Gosterme","El Hareketlerini Goster")

    def changeHandShow(self):
        mt._settings.handShow = not mt._settings.handShow
        self.changeHandShowText()

    def changeInformationShowText(self):
        self.changeShowText(mt._settings.information,2,"Bilgilendirmeyi Kapat","Bilgilendirmeyi Ac")

    def changeInformationShow(self):
        mt._settings.information = not mt._settings.information
        self.changeInformationShowText()

    def changeFlipModeShowText(self):
        self.changeShowText(mt._settings.isFlipMode,3,"Ters Ekrani \n Ac","Ters Ekrani \n Kapat")

    def changeFlipModeShow(self):
        mt._settings.isFlipMode = not mt._settings.isFlipMode
        self.changeFlipModeShowText()
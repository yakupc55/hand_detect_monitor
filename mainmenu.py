import cv2
import menuTools as mt
class MainMenu():
    def __init__(self,menu):
        self.menu = menu
        self.tabMenuRow = 0
        self.menuBackColor = (255,123,123)
        self.menuCount = 5
        self.childMenuWidth = 400
        self.childMenuHeight = 120
        self.space= 4
        self.menuList = []
        self.maxMenuWidth=0
        self.maxMenuHeight = 0
        menu.calculateMenuList(self)
        self.menuTextList = ["Menu Rengini Degistir",
        "El Hareketlerini Gosterme",
        "Bilgilendirmeyi Kapat",
        "Sayac : 0",
        "Degisen Yazi"]
        self.fontScale = 1.4
        self.textFont = cv2.FONT_HERSHEY_SIMPLEX
        self.textColor = (0, 255, 255)
        self.textThickness = 2
        self.textHeightSpace = 8
        self.textInfo =mt.TextSettings(0,0,0)
        menu.calculateTextForMultiLine(self.childMenuWidth,self.childMenuHeight,self.menuTextList,self.fontScale,self.textFont,self.textColor,self.textThickness,self.textHeightSpace,self.menuList,self.textInfo)
        self.sayac = 0
        self.colorCount =0
        self.colorList = [(255,123,123),(80,255,123),(14,80,210),(20,20,20),(240,240,240)]
        self.textCount=0
        self.textList=["Degisen Yazi","Merhaba","Kodlama Beni Gulum","Cilgin Yazilimci","Nasilsin?"]
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
            self.changeMenuColor()
        elif menuCode == 1:
            self.changeHandShow()
        elif menuCode == 2:
            self.changeInformationShow()
        elif menuCode == 3:
            self.changeCounter()
        elif menuCode == 4:
            self.randomText()
        else:
            print("its not a menu code")

    def changeCounter(self):
        self.sayac+=1
        newText = "Sayac : "+str(self.sayac)
        self.menuList[3].text = newText
        self.menuList[3].textCords = self.menu.calculateMenuTextForaItem(newText)
        #print("counter change")

    def changeMenuColor(self):
        self.colorCount += 1
        if self.colorCount > len(self.colorList) -1:
            self.colorCount =0
        self.menuBackColor = self.colorList[self.colorCount]
        for item in self.menuList:
            item.bgColor = self.menuBackColor

    def randomText(self):
        self.textCount += 1
        if self.textCount > len(self.textList)-1:
            self.textCount =0
        newText = self.textList[self.textCount]
        self.menuList[4].text = newText
        self.menuList[4].textCords = self.menu.calculateMenuTextForaItem(newText)

    def changeHandShow(self):
        mt._settings.handShow = not mt._settings.handShow
        if mt._settings.handShow:
            newText = "El Hareketlerini Gosterme"
        else:
            newText = "El Hareketlerini Goster"
        self.menuList[1].text = newText
        self.menuList[1].textCords = self.menu.calculateMenuTextForaItem(newText)
        
    def changeInformationShow(self):
        mt._settings.information = not mt._settings.information
        if mt._settings.information:
            newText = "Bilgilendirmeyi Kapat"
        else:
            newText = "Bilgilendirmeyi Ac"
        self.menuList[2].text = newText
        self.menuList[2].textCords = self.menu.calculateMenuTextForaItem(newText)
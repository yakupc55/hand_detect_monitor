import cv2
import mainmenu as main
import drawMenu
import menutestmenu
import settingsMenu
import detectObjectMenu
import ocrProcessMenu
import menuTools as mt
import time
class menus():
    def __init__(self):#constructor
        self.currentMenuNo = 5
        self.tabMenuWidth= 1280
        self.img = 0
        self.overlay = 0
        self.lmList = []
        self.lastIndex = -1
        self.clickControl = False
        self.clickColor = (255,0,0)


        self.mainMenu = main.MainMenu(self) #0
        self.settingsMenu = settingsMenu.SettingsMenu(self) #1
        self.menutestMenu= menutestmenu.MenuTestMenu(self) #2
        self.drawMenu = drawMenu.DrawMenu(self) #3
        self.detectObjectMenu = detectObjectMenu.DetectObjectMenu(self)#4
        self.ocrProcessMenu = ocrProcessMenu.OcrProcessMenu(self) #5
        self.changeCurrentMenu(self.currentMenuNo)
        self.lastTime =time.perf_counter()


    def changeCurrentMenu(self,code):
        self.lastIndex = -1
        if code == 0:
            self.currentMenuNo=0
            self.currentMenu = self.mainMenu
        elif code == 1:
            self.currentMenuNo=1
            self.currentMenu = self.settingsMenu
            self.currentMenu.firstOpen()
        elif code == 2:
            self.currentMenuNo=2
            self.currentMenu = self.menutestMenu
        elif code == 3:
            self.currentMenuNo=3
            self.currentMenu = self.drawMenu
            self.currentMenu.firstOpen()
        elif code == 4:
            self.currentMenuNo=4
            self.currentMenu = self.detectObjectMenu
            self.currentMenu.firstOpen()
        elif code == 5:
            self.currentMenuNo=5
            self.currentMenu = self.ocrProcessMenu
            self.currentMenu.firstOpen()
        else:
            self.currentMenuNo=0
            self.currentMenu = self.mainMenu

    def getxyCordinat(self):
        x1, y1 = self.lmList[8][1:]
        #x2, y2 = self.lmList[7][1:]
        #d = (x2-x1)/4
        d=8
        x1 = x1 -d
        y1 = y1 -d

        return x1,y1
    def cursorModeForMenu(self):
        x1, y1 = self.lmList[8][1:]
        #x2, y2 = self.lmList[7][1:]
        #d = (x2-x1)/4
        d=8
        x1 = x1 -d
        y1 = y1 -d
        #print("x1 : "+str(x1)+" y1 : "+str(y1))
        maxW = self.currentMenu.maxMenuWidth
        maxH = self.currentMenu.maxMenuHeight
        if(x1<=maxW and y1<=maxH):
            #print("its correct 1")
            #print("x1 : "+str(x1)+" y1 : "+str(y1))
            index = self.findChildNo(x1,y1)
            if index!=-1:
                #print("its working")
                self.currentMenu.menuList[index].bgColor = self.clickColor
                if index !=self.lastIndex:
                    self.changeLastIndex()
                self.lastIndex=index
        else:
            self.changeLastIndex()
            self.lastIndex = -1
                

    def changeLastIndex(self):
        if self.lastIndex>=0:
            self.currentMenu.menuList[self.lastIndex].bgColor = self.currentMenu.menuBackColor

    def clickaMenu(self):
        if self.clickControl:
            if self.lastIndex>=0:
                newTime = time.perf_counter()
                totalTime = newTime - self.lastTime
                if totalTime>0.25:
                    self.lastTime=newTime
                    self.currentMenu.clickaMenu(self.lastIndex)

    def fingerPress(self,key):
        if key == 2 or key ==6:
            self.cursorModeForMenu()
            self.clickControl = True
        else:
            self.changeLastIndex()
            self.lastIndex = -1
        if key == 3 or key == 7:
            self.cursorModeForMenu()
            self.clickaMenu()
            self.clickControl = False
        self.currentMenu.fingerPress(key)


    def drawFirst(self):
        self.currentMenu.drawFirst()
        return self.overlay

    def drawTabmenu():
        print("test")

    def lastDraw(self):
        print("test")
        
    def fillMenuList(self,cc,item):
        item.menuList.clear()
        for i in range(0,cc):
            item.menuList.append(mt.menuItem(i))

    def findChildNo(self,x,y):
        maxW = self.currentMenu.maxMenuWidth
        maxH = self.currentMenu.maxMenuHeight
        if x>= maxW:
            x = maxW-1
        if y>= maxH:
            y = maxH-1
        if x==0:
            x=1
        if y==0:
            y=1
        ch = self.currentMenu.childMenuHeight
        cc = self.currentMenu.menuCount
        cw = self.currentMenu.childMenuWidth
        rowC = maxW/cw
        column= int(x/cw)
        row = int(y/ch)
        index = (row*rowC)+column
        if(index<cc):
            return int(index)
        else:
            return -1

    def calculateMenuList(self,item):
        cc = item.menuCount
        cw = item.childMenuWidth
        ch = item.childMenuHeight
        self.fillMenuList(cc,item)
        isMultiLine = False
        x,y=0,0
        for i in range(0,cc):
            item.menuList[i].x = x
            item.menuList[i].y = y
            item.menuList[i].bgColor = item.menuBackColor

            x+=cw
            if x+cw > self.tabMenuWidth and i+1 != cc:
                if(y==0):
                    item.maxMenuWidth=x
                x=0
                y+=ch
                isMultiLine = True
        item.maxMenuHeight = y+ch
        if not isMultiLine:
            item.maxMenuHeight = ch
            item.maxMenuWidth = x
        # print(ch,cw,cc)
        # print(isMultiLine)
        # print(item.maxMenuWidth,item.maxMenuHeight)
            #print(item.menuList[i].no,item.menuList[i].x,item.menuList[i].y)

    def calculateMenuTextForaItem(self,newText):
        textHeight=self.currentMenu.textInfo.textHeight
        textFont = self.currentMenu.textFont
        fontScale = self.currentMenu.fontScale
        textThickness= self.currentMenu.textThickness
        cw = self.currentMenu.childMenuWidth
        ch = self.currentMenu.childMenuHeight
        spaceWidth = self.currentMenu.textInfo.spaceWidth
        textHeightSpace = self.currentMenu.textHeightSpace
        return self._calculateTextForMultiLine(newText,textHeight,textFont,fontScale, textThickness,cw,ch,spaceWidth,textHeightSpace)

    def _calculateTextForMultiLine(self,item,textHeight,textFont,fontScale, textThickness,cw,ch,spaceWidth,textHeightSpace):
        #print(i)
        texts= item.split(" ")
        #print(texts)
        list = []
        startx=0
        starty=textHeight
        rowText=""
        isMax=False
        totalDistance =0
        for idx,j in enumerate(texts):
            
            #print(j)
            distance = cv2.getTextSize(j,textFont,fontScale,textThickness)[0][0]
            #print(j+" : "+str(distance))
            totalDistance +=distance

            if totalDistance>cw or j=="\n":
                list.append(mt.TextCord(startx,starty,rowText))
                #print(rowText)
                if j=="\n": 
                    rowText=""
                else:
                    rowText=j+" "
                totalDistance=distance+ spaceWidth
                starty +=textHeight+textHeightSpace
                if starty>ch:
                    isMax = True
                    break
            else:
                rowText +=j+" "
                totalDistance+=spaceWidth
        #for add last one
        if  not isMax:
            list.append(mt.TextCord(startx,starty,rowText))
        return list

    def calculateTextForMultiLine(self,childMenuWidth,childMenuHeight,menuTextList,fontScale,textFont,textColor,textThickness,textHeightSpace,menuList,textInfo):
        #öncelikle boş bir sayfayı test ediyoruz
        #print(type(fontScale),type(textFont),type(textThickness))
        ch = childMenuHeight
        cw = childMenuWidth
        labelSize=cv2.getTextSize(" ",textFont,fontScale,textThickness)
        betweenSpace = 2
        #print(labelSize)
        spaceWidth = labelSize[0][0]-betweenSpace
        textHeight = labelSize[0][1]

        #change text info for later
        textInfo.betweenSpace=betweenSpace
        textInfo.spaceWidth=spaceWidth
        textInfo.textHeight=textHeight

        for index ,i in enumerate(menuTextList):
            list = self._calculateTextForMultiLine(i,textHeight,textFont,fontScale, textThickness,cw,ch,spaceWidth,textHeightSpace)
            menuList[index].textCords = list

        

    def drawMenus(self,overlay):
        list = self.currentMenu.menuList
        ch = self.currentMenu.childMenuHeight
        cc = self.currentMenu.menuCount
        cw = self.currentMenu.childMenuWidth
        cs = self.currentMenu.space
        color = self.currentMenu.menuBackColor
        cws = cw-cs
        for i in range(0,cc):
            #print(i)
            x, y, w, h = list[i].x+cs, list[i].y+cs, int(cws), ch-cs  # Rectangle parameters
            #print(x, y, w, h)
            cv2.rectangle(overlay, (x, y), (x+w, y+h), list[i].bgColor, -1)  # A filled rectangle
            fontScale = self.currentMenu.fontScale
            textFont = self.currentMenu.textFont
            textColor = self.currentMenu.textColor
            textThickness = self.currentMenu.textThickness
            # burda biz gelecek olan yazıyı yazdırmış oluyoruz
            for row in list[i].textCords:
                cv2.putText(overlay, row.text, (x,y+row.y), textFont, 
                   fontScale, textColor, textThickness, cv2.LINE_AA)
                #print(row.text)
            #labelSize=cv2.getTextSize("test",textFont,fontScale,textThickness)
            #print(labelSize)


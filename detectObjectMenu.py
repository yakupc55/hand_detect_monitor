from math import nan
import cv2
import numpy as np
import menuTools as mt

class DetectObjectMenu():
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

        #menün kendine ait değişkenleri
        self.net = nan
        self.model =nan
        self.classes = []

    def firstOpen(self):
        #net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
        net = cv2.dnn.readNet("dnn_model/yolov4-tiny-kalem_best.weights", "dnn_model/yolov4-tiny-kalem.cfg")
        # net = cv2.dnn.readNet("dnn_model/yolov4-tiny-obj.weights", "dnn_model/yolov4-tiny-obj.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(320, 320), scale=1/255)

        with open("dnn_model/classes.txt", "r") as file_object:
            for class_name in file_object.readlines():
                #print(class_name)
                class_name = class_name.strip()  # satır arası boşluklar için
                self.classes.append(class_name)
        print(len(self.classes))
        print(self.classes)
    def objectDetectionOnDraw(self,frame):
        # Object Detection
        (class_ids, scores, bboxes) = self.model.detect(frame, confThreshold=0.1, nmsThreshold=0.2)
        #print(class_ids)
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h) = bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200,0,50), 3)

            class_name = self.classes[class_id[0]]

            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200,0,50), 2)

 


    def fingerPress(self,key):
        if key == 8:
            print("working")

    def drawFirst(self):
        mt._settings.informationText = " obje tanima modu aktif(suan sadece kalem)"
        #print("its working")
        overlay = self.menu.img.copy()
        self.objectDetectionOnDraw(overlay)
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
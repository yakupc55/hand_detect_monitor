import cv2
import numpy as np
import time
import os
import handtrackingmodule as htm
import fingerprocess as fp
import menus as mn
import menuTools as mt

#burda parmak modlarını çekmek için kullandığımız bir fonksiyon
fingersMode = fp.fingerTools.fingersMode

#burda menu sistemini entegre ediyoruz
menu = mn.menus()
#bizim için en gerekli yapılardan biri kamera görüntüsünü yakalamak olacak
cap = cv2.VideoCapture(0)

#farklı bir yakalama sistemi var sanırım burda 1280*720 olarak belirledik ama bu hızlandırabilirmi bilmiyom ama şimdilik böyle kalsın
cap.set(3,1280)
cap.set(4,720)

activeMode = "none"
##########
##yazı yazmak için gerekli paremetreler
# font
textFont = cv2.FONT_HERSHEY_SIMPLEX
textOrg = (50, 700)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
textColor = (255, 0, 0)
  
# Line thickness of 2 px
textThickness = 2
#######
#sistemi çalıştırdığımız gibi sürekli olarak açık kalmasını sağlıyoruz.

#el hareketlerine algılayacak olan detektörümüz
detector = htm.handDetector(detectionCon=1,maxHands=1)

while True:
    #kameradan gelen bilgiyi belli bir yere yüklüyoruz
    #sucess kameradan bilgi alınıp alınamadığını söylüyor
    success, img = cap.read()

    #burda görüntüyü tersleme yapıyoruz
    img = cv2.flip(img,1)

    #el hareketlerinin okunması
    if mt._settings.handShow:
        img = detector.findHands(img)
    else:
        img = detector.findHands(img,draw =False)
    lmList = detector.findPosition(img,draw=False)
    menu.img = img
    
    #burda lm list parmak konumlarını tutuyor
    #lmlistde veri olup olmadığını kontrol ediyoruz ki sonradan sıkıntı çıkmasın
    if len(lmList)!=0 and len(lmList[0])!=0:
        #çok lu el modlarından dolayı 3 boyutlu olarak gelen veriden tek el verisini çekip ona eşitliyoruz
        lmList = lmList[0]
        menu.lmList = lmList
        #parmakların açık kapalığığını kontrol etme
        fingers = detector.fingersUp()
        listToStr = ' '.join(map(str, fingers))
        fingerCode = fingersMode(fingers)
        activeMode = " parmaklar :"+listToStr + " , finger Code :"+str(fingerCode)

        #test menu finger
        menu.fingerPress(fingerCode)
        img = menu.drawFirst()
    else:
        activeMode= "none"
        img = menu.drawFirst()
    #burda ekrana yazı yazdırıyor olacağız
    if mt._settings.information:
        img = cv2.putText(img, 'Active Mode : '+ activeMode, textOrg, textFont, 
                   fontScale, textColor, textThickness, cv2.LINE_AA)

    #burda yakalanan görüntüyü ekrana basıyoruz
    cv2.imshow("image",img)

    #görüntünün anlık olarak alına bilmesi için gerekli bir yapı
    cv2.waitKey(1)
class DrawMenu():
    def __init__(self,menu):
        self.menu = menu
    
    def fingerPress(self,key):
        print("draw menudesiniz")
        if key == 6:
            self.menu.changeCurrentMenu(0)
       
    def drawFirst(self):
        print("test")

    
import curses  
class cursor():
    posY = 0
    def __init__(self,posY) -> None:
        self.posY = posY
    def input(self,strstd):
        key = strstd.getkey()
        strstd.addstr(20,25,str(key))
        if(key == "w" or key == "KEY_UP"):
            self.posY-=1
        if(key == "s" or key == "KEY_DOWN"):
            self.posY += 1
        if(self.posY < 0):
            self.posY = 0
class console_panel():
    maxWidth =  55
    c = cursor(0)
    blocks = []  
    def run(self,strstd):
       while(True):
        self.render(strstd) 
        self.c.input(strstd)
    def render(self,strstd):
        #Yeni Dosyaya Tasinacak
        strstd.clear()
    def on_click(self):
        print("ONCLICKFUNCTION")

   
class block():
    x = 0
    y = 0
    text = ""
    hoverable = False 
    def __init__(self,x,y,text,hoverable) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.hoverable = hoverable

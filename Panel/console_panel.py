import curses  
class cursor():
    posY = 0
    def __init__(self,posY) -> None:
        self.posY = posY
    def input(self,strstd):
        key = strstd.getkey()
        strstd.addstr(50,25,str(key))
        if(key == "w" or key == "KEY_UP"):
            self.posY-=1
        if(key == "s" or key == "KEY_DOWN"):
            self.posY += 1
        if(self.posY < 0):
            self.posY = 0

class console_panel():
    blocks = []  
    maxWidth =  55
    currentlY = 0
    c = cursor(0)
    def run(self,strstd):
       while(True):
        self.render(strstd) 
        self.c.input(strstd)

        
    def render(self,strstd):
        strstd.clear()
        strstd.addstr(self.c.posY,0,"####################################")
        for i in self.blocks:
            strstd.addstr(i.y,i.x,str(i.text))
            if(i.y == self.c.posY and i.hoverable == True):
                strstd.addstr(50,100,"Clickable")
        strstd.refresh()
        strstd.getch()

    def draw_new(self,text,hoverable):
        self.currentlY += 3
        tempBlock = block(0,self.currentlY,text,hoverable)
        self.blocks.append(tempBlock)
   
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

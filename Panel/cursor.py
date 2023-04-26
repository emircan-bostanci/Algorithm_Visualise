from enum import Enum
class cursor:
    cursorX = cursorY = 0
    blocks = []
    strstd = None
    def __init__(self,strstd,blocks) -> None:
        self.blocks.extend(blocks)
        self.strstd = strstd

    def keyboard_input(self):
        key = self.strstd.getkey()
        if(key == 'w'):
            self.cursorY += 1
        if(key == 'a' and self.cursorX > 0):
            self.cursorX -= 1
        else:
            self.keyboar_order(key)
            
    def keyboar_order(self,key):
        if(key == 'q'):
            return orders.QUIT
        if(key == 'r'):
            return orders.RESET
        if(key == 'b'):
            return orders.BACK
        
class orders(Enum):
    QUIT = 0
    RESET = 1
    BACK = 2
    
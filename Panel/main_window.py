from Panel import console_panel
from importer import importer 

class main_window(console_panel.console_panel):

    cursor = console_panel.console_panel.c
    currentlY = 0
    algorithms = []
    def __init__(self):
        self.implement_algorithm()
        self.run_algorithms()
    def implement_algorithm(self):
        self.imports =importer("./Algorithms") 
        self.imports.import_all()
        self.algorithms.extend(self.imports.files)
    def run_algorithms(self):
        tmpList = [4,255,14,24,22,35,3]
        for i in self.algorithms:
            label = i.info()
            self.draw_new(label,True)


    def render(self,strstd):
        console_panel.console_panel.render(self,strstd)
        strstd.addstr(self.cursor.posY,0,"####################################")
        for i in self.blocks:
            strstd.addstr(i.y,i.x,str(i.text))
            if(i.y == self.c.posY and i.hoverable == True):
                strstd.addstr(40,100,i.text + " Display (Click Space)")
        strstd.refresh()
        strstd.getch()
    def on_click(self,func):
        console_panel.console_panel.on_click(self)
    def draw_new(self,text,hoverable):
        self.currentlY += 1
        tempBlock = console_panel.block(0,self.currentlY,text,hoverable)
        console_panel.console_panel.blocks.append(tempBlock)



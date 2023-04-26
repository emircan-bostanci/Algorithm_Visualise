import curses
import time
import random
from curses import wrapper

class window():
    algorithm = None
    phase = 0
    def windows_size(self,stdstr):
        x = 0
        y = 0
        curses.getmaxyx(stdstr,x,y)
        return {x,y}
    def __init__(self,algorithm) -> None:
        self.algorithm = algorithm
        print(algorithm.info())
        tempList = []
        for i in range(0,200):
            tempList.append(random.randint(0,40))
        self.algorithm.run(tempList)
        wrapper(self.run)
    def run(self, strscr):
        while(True):
            strscr.clear()
            self.render(strscr)
            self.update()

    def render(self,strscr):
        #TODO Settings File
        curses.curs_set(0)
        strscr.addstr(0,0,self.algorithm.info())
        strscr.addstr(1,0,str(len(self.algorithm.roads)))
        index = 0
        self.color_settings()
        for j in range(0,len(self.algorithm.roads[self.phase])):
            for k in range(0,self.algorithm.roads[self.phase][j]):
                #TODO ayarlar sayfasina genislik treshold
                strscr.addstr(50 - k,(j+5)*1, ' ',curses.color_pair(int(self.algorithm.roads[self.phase][j] * 5)))
        index+=1
        strscr.refresh()
    def color_settings(self):
        curses.start_color()
        curses.use_default_colors()
        for i in range(0,255):
            curses.init_pair(i+1,-1,i)
    def update(self):
        if(self.phase < len(self.algorithm.roads)-1):
            self.phase += 1

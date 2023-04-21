import curses
import time
from curses import wrapper

class window():
    algorithm = None
    phase = 0
    def __init__(self,algorithm) -> None:
        self.algorithm = algorithm
        print(algorithm.info())
        tempList = [13,23,4,24,5]
        self.algorithm.run(tempList)
        wrapper(self.run)
    def run(self, strscr):
        while(True):
            self.render(strscr)
            self.update()
            time.sleep(1.5)

    def render(self,strscr):
        strscr.addstr(0,0,self.algorithm.info())
        strscr.addstr(1,0,str(len(self.algorithm.roads)))
        index = 0
        strscr.clear()
        for j in range(0,len(self.algorithm.roads[self.phase])):
            for k in range(0,self.algorithm.roads[self.phase][j]):
                strscr.addstr(40 - k,(j+10)*3, '#')
                strscr.addstr(15,(index + 15) * 3,str(self.algorithm.roads[self.phase][j]))
        index+=1
        strscr.addstr(5,5,str(self.algorithm.roads[1]))
        strscr.refresh()
    
    def update(self):
        if(self.phase < len(self.algorithm.roads)-1):
            self.phase += 1

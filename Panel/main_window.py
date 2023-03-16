from Panel import console_panel

class main_window(console_panel.console_panel):
    def render(self,strstd):
        console_panel.console_panel.render(self,strstd)
        for i in self.blocks:
            strstd.addstr(i.y,i.x,str(i.text))
            if(i.y == self.c.posY and i.hoverable == True):
                strstd.addstr(40,100,"Clickable")
        strstd.refresh()
        strstd.getch()

    def on_click(self):
        console_panel.console_panel.on_click(self)




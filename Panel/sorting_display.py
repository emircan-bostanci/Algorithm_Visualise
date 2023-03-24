from Panel.console_panel import console_panel

class sorting_display(console_panel):
    currently_algorithm = None
    def __init__(self,currently_algorithm):
        self.currently_algorithm = currently_algorithm
    def render(self):
        console_panel.render()
    def visualise(self):
        steps = 0
        for i in range(steps):
            print(steps)



    

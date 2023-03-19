class display_manager:
    currently_display = None 
    def __init__(self,display):
        self.change_display(display)
    def get_display(self):
        return self.currently_display;
    def change_display(self,display):
        self.currently_display = display


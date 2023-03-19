from Panel import console_panel
from Panel import main_window 
from curses import wrapper


#Eger algoritmalar dosyasinda kosullari saglayan dosya varsa implemente edilir
#Yeni eklenen algoritma dosyasinda run isimli fonksiyon bulunmali 
#display = console_panel.console_panel()

def main():
    display = main_window.main_window()
    wrapper(display.run)
main()

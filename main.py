from Panel import console_panel
from Panel import main_window 
from Panel.display_manager import display_manager


#Eger algoritmalar dosyasinda kosullari saglayan dosya varsa implemente edilir
#Yeni eklenen algoritma dosyasinda run isimli fonksiyon bulunmali 
#display = console_panel.console_panel()
def main():
    global display_manager
    display_manager = display_manager(main_window.main_window())
    
     

main()

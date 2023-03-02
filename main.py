from importer import importer 
from Panel import console_panel
from curses import wrapper


algorithms = []
#Eger algoritmalar dosyasinda kosullari saglayan dosya varsa implemente edilir
#Yeni eklenen algoritma dosyasinda run isimli fonksiyon bulunmali 
display = console_panel.console_panel()
def implement_algorithm():
    imports =importer("./Algorithms") 
    imports.import_all()
    algorithms.extend(imports.files)

def run_algorithms():
    tmpList = [4,255,14,24,22,35,3]
    for i in algorithms:
        label = i.info()
        text = i.run(tmpList)
        display.draw_new(label,True)
        display.draw_new(text,False)
def main():
    implement_algorithm()
    run_algorithms()
    wrapper(display.run)
main()
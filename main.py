from importer import importer
from Panel.window import window
from rich import print as rprint  

algorithm_importer = importer('./Algorithms')
algorithm_importer.import_all()
def algorithm_selection():
    for i in range(0,len(algorithm_importer.files)):
        rprint(str(i) + ") [red] " + algorithm_importer.files[i].info())
    selected_algorihm = input("Select One : ")
    selected_algorihm = int(selected_algorihm)
    if(selected_algorihm > len(algorithm_importer.files)):
        print("Select exist algorithm")
        algorithm_selection()
    return int(selected_algorihm)
def import_algorithm():
    pass
seleced = algorithm_selection()
selection_window = window(algorithm_importer.files[seleced
                                                   ])

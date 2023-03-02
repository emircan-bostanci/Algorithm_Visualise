import os;
import importlib.util
import sys;

class importer:
    files = []
    def __init__(self,folderPath):
        self.folderPath = folderPath
    def import_all(self):
        tempFiles = os.listdir(self.folderPath) 
        for i in tempFiles:
            if(os.path.isfile(self.folderPath+"/"+i) and os.path.splitext(i)[1] == ".py"):
                spec = importlib.util.spec_from_file_location(i,self.folderPath+"/"+i)
                run = importlib.util.module_from_spec(spec) 
                sys.modules[i] = run
                spec.loader.exec_module(run)
                self.files.append(run)
        
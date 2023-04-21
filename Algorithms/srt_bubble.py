data= []
step = 0
roads = []
def algorithm(step):
    strList = ""
    if(step != 3):
        for i in range(0,len(data)-1):
            for j in range(i,len(data)):
               if(data[i] < data[j]):
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
                roads.append(data.copy())
    for i in range(0,len(data)):
        strList += str(data[i])+" "
    data.reverse()
    return data
def run(dataset):
    data.extend(dataset) 
    algorithm(0)
    print(roads)
    return data
def get_roads(self):
    return self.roads

def info():
    return "Bubble Sort"

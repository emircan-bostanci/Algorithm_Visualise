data= []
step = 0
def algorithm(step):
    strList = ""
    if(step != 3):
        for i in range(0,len(data)-1):
            for j in range(i,len(data)):
               if(data[i] < data[j]):
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
    for i in range(0,len(data)):
        strList += str(data[i])+" "
    data.reverse()
    return data
    info()
def run(dataset):
    data.extend(dataset) 
    algorithm(0)
    return data
def info():
    return "Bubble Sort"

dataset = [] 
roads = []
def algorithm():
   for i in range(1,len(dataset)):
        selected = dataset[i]
        j = i - 1
        while j >= 0 and selected< dataset[j]:  
            dataset[j+1] = dataset[j]  
            j -= 1  
        dataset[j+1] =selected 


def run(data):
    for i in data:
        dataset.append(i)
    algorithm()
    return dataset

def info():
    return("(BUG) Insertion Sort")

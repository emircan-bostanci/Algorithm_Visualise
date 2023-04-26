import math


dataset = []
roads = []

def algorithm():
    gap = math.floor(len(dataset) / 2)
    while(gap > 0):
        gap = math.floor(gap / 2)
        for index in range(gap,len(dataset)):
            tempIndex = index
            item = dataset[index]
            while(tempIndex >= gap and dataset[tempIndex - gap] > item):
                dataset[tempIndex] = dataset[tempIndex - gap]
                tempIndex = tempIndex-  gap
            dataset[tempIndex] = item

def run(data):
    dataset.extend(data)
    algorithm()
    return dataset
def get_roads(self):
    return roads


def info():
    return("(BUG) Shell Sort")

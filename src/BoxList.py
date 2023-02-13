class BoxList:
    boxes = [] #Box array
    fitness = int()
    boxWeight = int()

    def __init__(self, boxArray, boxWeight):
        self.boxes = boxArray
        self.boxWeight = boxWeight
        self.getFitness()

    def generateLocalSearch(self) -> "BoxList":
        currentList = self.boxes
        newListLenght = len(currentList)
        newList = currentList

        boxPosition = 0
        for box in currentList:
            if(boxPosition >= 1):
                if(len(newList[boxPosition - 1]) <= 1):
                    newList.pop(0)
                    newListLenght = len(newList)
                    boxPosition -= 1
            for item in box:
                index = 0
                while(True):
                    index += 1
                    position = len(newList) - index
                    if(newList[boxPosition - 1] == 0):
                        position += 1
                    print(len(newList), position, boxPosition)
                    if(position <= boxPosition):
                        break
                    if(self.getBoxWeight(position, newList) + item <= self.boxWeight):
                        newList[position].append(item)
                        newList[boxPosition].pop(0)
                        break
            boxPosition += 1
            print(newList)
        return(newList)

    def getBoxWeight(self, index, passedList):
        if(index >= len(passedList)):
            index -= 1
        currentBox = passedList[index]
        currentWeight = 0
        for item in currentBox:
            currentWeight += item
        return currentWeight
    
    def findNeighbors(self) -> list("BoxList"):
        pass

    def getFitness(self):
        pass



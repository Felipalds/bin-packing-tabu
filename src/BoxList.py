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
        for boxPosition, box in enumerate(currentList):
            if(boxPosition >= 1):
                if(len(newList[boxPosition - 1]) <= 1):
                    newList.pop(0)
                    newListLenght -= 1
            isAdded = False
            for itemPosition, item in enumerate(box):
                if(isAdded):
                    newList[boxPosition].pop(0)

                isAdded = False
                index = 0
                while(not isAdded):
                    index += 1
                    position = newListLenght - index
                    if(position < boxPosition):
                        break
                    if(self.getBoxWeight(position, newList) + item <= self.boxWeight):
                        isAdded = True
                        newList[position].append(item)
                        break

        return(newList)

    def getBoxWeight(self, index, passedList):
        if(index >= len(passedList)):
            index -= 1
        currentBox = passedList[index]
        currentWeight = 0
        for item in currentBox:
            currentWeight += item
        return currentWeight
    
    def generateEmptyList(self, length):
        newList = []
        for c in range(length):
            newList.append([])
        return newList

    def findNeighbors(self) -> list("BoxList"):
        pass

    def getFitness(self):
        pass



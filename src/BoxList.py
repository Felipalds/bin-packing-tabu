class Box:
    items = []

    def __init__(self, items_list : list[int]):
        self.items = items_list

    def __repr__(self) -> str:
        return str(self.items)

    def getWeight(self) -> int:
        return sum(self.items)

    def __eq__(self, __o : object) -> bool:
        if __o.items.sort() == self.items.sort():
            return True
        else:
            return False

class BoxList:
    fitness = int()
    max_weight = int()

    def __init__(self, max_weight : int, boxes : list[Box]):
        self.boxes = boxes
        self.max_weight = max_weight
        self.fitness = len(boxes)

    def __repr__(self) -> str:
        init_string = f"W{self.max_weight}|B{len(self.boxes)}"
        init_string += f" {self.boxes}"
        return init_string
    
    def __eq__(self, __o: object) -> bool:
        if __o.boxes == self.boxes:
            return True
        else:
            return False

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

    




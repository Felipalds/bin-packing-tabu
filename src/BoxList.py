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

    def generateLocalSearch(self) -> list["BoxList"]:
        pass

    def findNeighbors(self) -> list["BoxList"]:
        pass

    def getFitness(self):
        pass

    




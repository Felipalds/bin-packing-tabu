import copy

class Box:
    items = []

    def __init__(self, items_list):
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

    def __init__(self, max_weight : int, boxes):
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

    def findneighbor(self) -> "BoxList": 
        list_array = self.boxes
        aux_tam = len(list_array)-1
        list_neighbor = []
        while aux_tam > -1:
            if len(list_array[aux_tam].items) > 1:
                new_box = list_array[aux_tam].items.pop()
                list_array.insert(0, Box([new_box,]))
                list_neighbor.append(copy.deepcopy(list_array))
                aux_tam = len(list_array)-1 
            else:
                aux_tam -= 1
        return(list_neighbor)

    def getBoxWeight(self, index, passedList):
        if(index >= len(passedList)):
            index -= 1
        currentBox = passedList[index]
        currentWeight = 0
        for item in currentBox:
            currentWeight += item
        return currentWeight

    def getFitness(self):
        pass

box_list = BoxList(30, [Box([1,2]), Box([3,4,5]), Box([6,7,8]), Box([9, 10, 11])])
array = [box.items for box in box_list.boxes]
list_neighbor = box_list.findneighbor()
print(list_neighbor)
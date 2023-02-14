import copy

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

    def copy(self):
        return BoxList(self.max_weight, self.boxes)

    def generateLocalSearch(self) -> "BoxList":
        currentList = self.boxes
        newList = currentList.copy()

        isAdded = True
        while(len(newList[0].items) == 1 and isAdded):
            for j, backbox in enumerate(reversed(newList)):
                if(j == len(newList) - 1):
                    isAdded = False
                    break
                if(backbox.getWeight() + newList[0].items[0] <= self.max_weight):

                    backbox.items.append(newList[0].items[0])
                    newList.pop(0)
                    break
                
        return(BoxList(self.max_weight, newList))

    
    def findNeighbors(self) -> list("BoxList"): 
        list_array = self.boxes
        aux_tam = len(list_array)-1
        list_neighbor = []
        while aux_tam > -1:
            if len(list_array[aux_tam].items) > 1:
                new_box = list_array[aux_tam].items.pop()
                list_array.insert(0, Box([new_box,]))
                list_neighbor.append(copy.deepcopy(BoxList(self.max_weight, list_array)))
                aux_tam = len(list_array)-1 
            else:
                aux_tam -= 1
        return(list_neighbor)


    def getFitness(self):
        pass

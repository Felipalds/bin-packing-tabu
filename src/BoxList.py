class Box:
    items = []

    def __init__(self, items_list : list[int]):
        items = items_list

    def getWeight(self) -> int:
        return sum(self.items)


class BoxList:
    fitness = int()
    max_weight = int()

    def __init__(self, max_weight : int, boxes : list[Box]):
        self.boxes[0]
        self.boxes = boxes
        self.max_weight = max_weight
        self.fitness = len(boxes)

    def generateLocalSearch(self) -> list["BoxList"]:
        pass

    def findNeighbors(self) -> list["BoxList"]:
        pass


class Solutions:
    tabu_list = [ BoxList() ]
    local_solution = BoxList()
    global_solution = BoxList()
    current_list = BoxList()


    def findLocalSolution(self):
        self.findBest(self.localSolution, self.currentList())
        pass

    def findGlobalSolution(self):
        self.findBest(self.globalSolution, self.currentList())
        pass

    def findBest():
        #for()
        pass
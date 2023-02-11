
class Box:
    items = []
    max_weight = int()

    def __init__(self):
        pass


class BoxList:
    boxes = [ Box ]
    fitness = int()
    box_weight = int()

    def __init__(self):
        self.boxes = []

    def generateLocalSearch(self) -> list("BoxList"):
        pass
    def findNeighbors(self) -> list("BoxList"):
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
class BoxList:
    boxes = [] #Box array
    fitness = int()
    box_weight = int()

    def __init__(self, boxArray):
        self.boxes = boxArray
        self.getFitness()

    def generateLocalSearch(self) -> list("BoxList"):
        pass

    def findNeighbors(self) -> list("BoxList"):
        pass

    def getFitness(self):
        pass



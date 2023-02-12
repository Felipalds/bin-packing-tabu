from BoxList import BoxList

class Solutions:
    tabu_list = {}
    local_solution = BoxList()
    global_solution = BoxList()
    current_list = BoxList()

    def __init__(self, initial_solution : BoxList = None):
        self.global_solution = initial_solution
        self.local_solution = initial_solution
        self.current_list = initial_solution

    def add_tabu(self, box_list : BoxList, tabu_count : int = 3):
        self.tabu_list[box_list] = tabu_count

    def advance_tabu(self):
        for key in self.tabu_list.keys():
            self.tabu_list[key] -= 1
            if self.tabu_list[key] <= 0:
                del self.tabu_list[key]

    def findLocalSolution(self):
        self.findBest(self.localSolution, self.currentList())
        pass

    def findGlobalSolution(self):
        self.findBest(self.globalSolution, self.currentList())
        pass

    def findBest():
        #for()
        pass
from BoxList import BoxList

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
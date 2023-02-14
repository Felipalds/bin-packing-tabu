from BoxList import BoxList

class Solutions:
    tabu_list = []

    def __init__(self, initial_solution : BoxList = None, tabu_length : int = 3):
        self.tabu_list = []
        self.global_solution = initial_solution
        self.local_solution = initial_solution
        self.current_list = initial_solution
        self.tabu_length = tabu_length

    def add_tabu(self, box_list : BoxList):
        if len(self.tabu_list) > self.tabu_length:
            del self.tabu_list[0]
        self.tabu_list.append(box_list)

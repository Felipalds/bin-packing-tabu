import sys
from Solutions import Solutions
from BoxList import BoxList, Box

arguments = sys.argv[:]
file_name = arguments[1]
with open(file_name, 'r') as file_handle:
    max_weight = int(file_handle.readline())
    item_amount = int(file_handle.readline())
    box_list = BoxList(max_weight, [Box([int(item),]) for item in file_handle.readline().split()])
    step = 0
    max_steps = int(input("Insert max steps: "))
    tabu_count = int(input("Insert tabu count: "))
    solutions = Solutions(box_list.generateLocalSearch())
    print(f"== STEP {step} ==")
    print(f"Worst Solution: {box_list}")
    print(f"Global Solution: {solutions.global_solution}\n")
    print(f"Local Solution: {solutions.local_solution}\n")
    print(f"Tabu List: {solutions.tabu_list}\n")
    while (step < max_steps):
        print(f"-- NEIGHBORS --")
        neighbors = BoxList.findNeighbors(box_list)
        for neighbor in neighbors: print(neighbor)
        opt_neighbors = [neighbor.generateLocalSearch() for neighbor in neighbors]
        print(f"-- NEIGHBORS (LS) --")
        for neighbor in opt_neighbors: print(neighbor)
        solutions.local_solution = opt_neighbors[0]
        for neighbor in opt_neighbors[1:]:
            if not neighbor in solutions.tabu_list:
                if neighbor.fitness >= solutions.global_solution.fitness:
                    solutions.global_solution = neighbor
                if neighbor.fitness >= solutions.local_solution.fitness:
                    solutions.local_solution = neighbor
                solutions.advance_tabu()
                solutions.add_tabu(solutions.local_solution, tabu_count)
        print(f"== STEP {step} ==")
        print(f"Global Solution: {solutions.global_solution}\n")
        print(f"Local Solution: {solutions.local_solution}\n")
        print(f"Tabu List: {solutions.tabu_list}\n")
                
        
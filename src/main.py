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
local_searched = box_list.generateLocalSearch()
solutions = Solutions(local_searched)
solutions.current_list = local_searched
solutions.add_tabu(solutions.current_list)
print("LOCAL SEARCHED:", local_searched)
print("LOCAL SEARCH!: ", solutions.current_list)
print(f"== STEP {step} ==")
print(f"Worst Solution: {box_list}")
print(f"Global Solution: {solutions.global_solution}\n")
print(f"Local Solution: {solutions.local_solution}\n")
print(f"Tabu List: {solutions.tabu_list}\n")
while (step < max_steps):
    print("CURRENT LIST : ", solutions.current_list)
    neighbors = solutions.current_list.findNeighbors()
    print("-- NEIGHBORS -- ")
    for neighbor in neighbors:
        print(neighbor)
    print(len(neighbors))
    local_searched_neighbors = [neighbor.generateLocalSearch() for neighbor in neighbors]
    print(f"-- NEIGHBORS (LS) --")
    print(len(local_searched_neighbors))
    for neighbor in local_searched_neighbors:
        print(neighbor)
    for searched in local_searched_neighbors:
        if not searched in solutions.tabu_list:
            solutions.local_solution = searched
            break
    for searched in local_searched_neighbors:
        if not searched in solutions.tabu_list:
            if searched.fitness <= solutions.global_solution.fitness:
                solutions.global_solution = searched
            if searched.fitness < solutions.local_solution.fitness:
                solutions.local_solution = searched
                solutions.current_list = searched
            solutions.add_tabu(solutions.local_solution)
    step += 1
    print(f"== STEP {step} ==")
    print(f"Global Solution: {solutions.global_solution}\n")
    print(f"Local Solution: {solutions.local_solution}\n")
    print(f"Tabu List: {solutions.tabu_list}\n")
            
    
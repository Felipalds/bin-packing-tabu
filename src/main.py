import sys
from Solutions import Solutions
from BoxList import BoxList, Box
import copy

arguments = sys.argv[:]
file_name = arguments[1]
with open(file_name, 'r') as file_handle:
    max_weight = int(file_handle.readline())
    item_amount = int(file_handle.readline())
    box_list = BoxList(max_weight, [Box([int(item),]) for item in file_handle.readline().split()])
step = 0
max_steps = int(input("Insert max steps: "))
tabu_max = int(input("Insert tabu max: "))
local_searched = box_list.generateLocalSearch()
local_solution = local_searched.copy()
global_solution = local_searched.copy()
tabu_list = []
print(local_solution, global_solution)
while (step < max_steps):
    print(f"==STEP {step}==")
    print(f"Local solution: {local_solution}")
    print(f"Global solution: {global_solution}")
    local_searched_neighbors = [neighbor.generateLocalSearch() for neighbor in local_solution.findNeighbors()]
    # for n in local_searched_neighbors: print(n)
    for searched in local_searched_neighbors:
        if not searched in tabu_list:
            local_solution = searched.copy()
            break
    for searched in local_searched_neighbors:
        # print("SEARCH:",searched)
        if not searched in tabu_list:
            if searched.fitness < local_solution.fitness:
                local_solution = searched.copy()
                if len(tabu_list) == tabu_max:
                    tabu_list.pop(0)
                tabu_list.append(local_solution)
            print(searched.fitness, global_solution.fitness)
            if searched.fitness <= global_solution.fitness:
                # print(searched.fitness, global_solution.fitness)
                # print("OMG", searched)
                global_solution = local_solution
                # print("OMG2:",global_solution)
    step += 1
    
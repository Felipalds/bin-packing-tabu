# Unidimensional package using tabu search

## Explanation

## Data structures

```
    class BoxesLists {
        fitness: number;
        Box: ItemList;
        lenght: int;
        first: ItemList;
        last: ItemList;
    }

    class ItemList{
        lenght: int;
        first: *Node;
        last: *Node;
        next: ItemList;
        previous: ItemList;
    }

    class Node {
        value: int;
        next: *Node;
        previous: *Node;
    }

    class Solutions {
        local: BoxesList;
        global: BoxesLists;
    }

    Boxes tabuList[n]

    while(ponto de parada nao cumprido):
        for neighbor in neighbors [ solucaoinicial ]:
            localsearch = boxlist.generatelocalSearch()
            solution.findBests(localsearch)
        neighbors = local_best.findNeighbors(solution)

```

## Pseudoalgorithm
1. Inputs
   - box maximum weight
   - items amount
   - weight of each item
2. Local search (greedy algorithm)
   - Join items in same boxes
3. For each solution, find the local search again to see if it is in the tabu list
4. Verify if solution is local best or global best
5. Replace the local and/or global best solution
6. Add solution to tabu list
7. Verify stop


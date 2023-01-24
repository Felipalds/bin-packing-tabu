# Unidimensional package using tabu search

## Data structures

```
    class Boxes {
        fitness: number;
        array : [number];
    }

    class Solutions {
        local: Boxes;
        global: Boxes;
    }

    Boxes tabuList[n]

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


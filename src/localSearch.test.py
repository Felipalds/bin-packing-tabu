from BoxList import BoxList

def __main__():
    currentBoxes = BoxList([[2],[2],[1],[2],[3],[3],[4]], 6)
    localSearchArray = currentBoxes.generateLocalSearch()
    print(localSearchArray)
    
    currentBoxes2 = BoxList([[1],[2],[3, 2],[3, 2],[4]], 6)
    localSearchArray = currentBoxes2.generateLocalSearch()
    print(localSearchArray)

    currentBoxes3 = BoxList([[2],[1],[2],[3, 2],[3],[4]], 6)
    localSearchArray = currentBoxes3.generateLocalSearch()
    print(localSearchArray)

__main__()
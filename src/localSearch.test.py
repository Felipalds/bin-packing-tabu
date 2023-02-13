from BoxList import BoxList

def __main__():
    currentBoxes = BoxList([[1],[2],[3, 2],[3, 2],[4]], 6)
    print(currentBoxes.boxes)
    localSearchArray = currentBoxes.generateLocalSearch()
    print(localSearchArray, "\n")
    
    currentBoxes2 = BoxList([[2],[1],[2],[3, 2],[3],[4]], 6)
    print(currentBoxes2.boxes)
    localSearchArray = currentBoxes2.generateLocalSearch()
    print(localSearchArray, "\n")

    currentBoxes3 = BoxList([[2],[2],[1],[2],[3],[3],[4]], 6)
    print(currentBoxes3.boxes)
    localSearchArray = currentBoxes3.generateLocalSearch()
    print(localSearchArray, "\n")

    # currentBoxes4 = BoxList([[11], [11], [12],[4],[3],[11],[9],[3],[3],[20],[15],[19],[18],[8],[2],[19],[11],[2],[3],[7]], 20)
    # print(currentBoxes4.boxes)
    # localSearchArray = currentBoxes4.generateLocalSearch()
    # print(localSearchArray, "\n")
__main__()
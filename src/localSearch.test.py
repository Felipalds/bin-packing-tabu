from BoxList import BoxList
from BoxList import Box

def __main__():
    box1 = Box([1])
    box2 = Box([2])
    box3 = Box([3, 2])
    box4 = Box([3, 2])
    box5 = Box([4])

    currentBoxes = BoxList(6, [box1, box2, box3, box4, box5])
    print(currentBoxes.boxes)
    localSearchArray = currentBoxes.generateLocalSearch()
    print(localSearchArray, "\n")
    
    box1 = Box([2])
    box2 = Box([1])
    box3 = Box([2])
    box4 = Box([3, 2])
    box5 = Box([3])
    box6 = Box([4])
    currentBoxes2 = BoxList(6, [box1, box2, box3, box4, box5, box6])
    print(currentBoxes2.boxes)
    localSearchArray = currentBoxes2.generateLocalSearch()
    print(localSearchArray, "\n")


    box1 = Box([2])
    box2 = Box([2])
    box3 = Box([1])
    box4 = Box([2])
    box5 = Box([3])
    box6 = Box([3])
    box7 = Box([4])

    currentBoxes3 = BoxList(6, [box1, box2, box3, box4, box5, box6, box7])
    print(currentBoxes3.boxes)
    localSearchArray = currentBoxes3.generateLocalSearch()
    print(localSearchArray, "\n")

    # currentBoxes4 = BoxList([[11], [11], [12],[4],[3],[11],[9],[3],[3],[20],[15],[19],[18],[8],[2],[19],[11],[2],[3],[7]], 20)
    # print(currentBoxes4.boxes)
    # localSearchArray = currentBoxes4.generateLocalSearch()
    # print(localSearchArray, "\n")
__main__()
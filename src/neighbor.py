from BoxList import BoxList
import copy


def findneighbor(list_array): 
    aux_tam = len(list_array)-1
    list_neighbor = []
    while aux_tam > -1:
        if len(list_array[aux_tam]) > 1:
            new_box = list_array[aux_tam].pop()
            list_array.insert(0, [new_box])
            list_neighbor.append(copy.deepcopy(list_array))
            aux_tam = len(list_array)-1
            
        else:
            aux_tam -= 1
    return(list_neighbor)

array_teste = [[1,2],[3,4,5],[6,7,8], [9, 10, 11], [12]]
vizinhos = findneighbor(array_teste)
print(vizinhos)
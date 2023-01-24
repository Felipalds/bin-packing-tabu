#include <iostream>
#include <stdlib.h>


class Node{
        
};
class List
{   
    Node next;
};

class Boxes {
    public:
        int fitness;
        int **Items = (int**) malloc(sizeof(int*));
        
        Boxes(int fitness)
        {
            fitness = fitness;
            
        }
};



int main() 
{
    std::cout << "Hello World!";
    return 0;
}
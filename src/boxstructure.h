#ifndef ANIMALS
#define ANIMALS

#include <iostream>
#include <vector>
using namespace std;

class BoxList
{
    private:

    public:
        vector<vector<int>> *boxes = new vector<vector<int>>;
        // public methods
        int get_fitness()
        {
            int fitness = (*boxes).size();
            return fitness;
        }
        int get_weight(int index)
        {
            if (index < 0)
                index = (*boxes).size() + index;
            int sum = 0;
            for (int n : (*boxes)[index])
                sum += n;
            return sum;
        }
        BoxList copy()
        {
            BoxList new_box_list;
            for (vector<int> n : (*boxes))
            {
                (*new_box_list.boxes).push_back(n);
            }
            return new_box_list;
        }
        bool operator==(BoxList rhs)
        {
            if ((*boxes) == (*rhs.boxes))
                return 1;
            return 0;
        }
};

class Solutions
{
public:
    BoxList global_solution;
    BoxList local_solution;
    vector<BoxList> tabu_list;
    BoxList find_optimal(vector<BoxList>)
    {
        return BoxList();
    }
};

void test_method()
{
    BoxList box_list;
    (*box_list.boxes).push_back(vector<int>{4, 4});
    (*box_list.boxes).push_back(vector<int>{3, 9});
    BoxList box_list_two;
    (*box_list_two.boxes).push_back(vector<int>{4, 4});
    (*box_list_two.boxes).push_back(vector<int>{3, 9});
    BoxList box_list_copy = box_list.copy();
    (*box_list_copy.boxes).push_back(vector<int>{10, 10});
    cout << "Is box_list_copy equal to box_list?: " << (box_list_copy == box_list) << '\n';
    cout << "Is box_list equal to box_list_two?: " << (box_list == box_list_two) << '\n';
    cout << "box_list's first box's weight: " << box_list.get_weight(0) << '\n';
    (*box_list_copy.boxes)[0].erase((*box_list_copy.boxes)[0].begin() + 1);
    cout << "box_list_copy's first box's weight: " << box_list_copy.get_weight(0) << '\n';
}

#endif
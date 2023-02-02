#include "boxstructure.h"
#include "binpack.h"
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

BoxList bin_pack_from_file( // Reads max_weight\nitem_amount\nitem\u0009item2... file format
    string file_name,
    int& max_weight,
    int& item_amount)
{
    ifstream file_stream(file_name);
    string read_buffer;
    getline(file_stream, read_buffer);
    max_weight = stoi(read_buffer);
    getline(file_stream, read_buffer);
    item_amount = stoi(read_buffer);
    getline(file_stream, read_buffer);
    BoxList new_box_list;
    vector<vector<int>> n_vector;
    string n_constructor;
    int box_index = 0;
    for (char c : read_buffer)
    {
        if (c != '\u0009') 
        {
            n_constructor += c;
        }
        else
        {
            n_vector.push_back(vector<int>{});
            n_vector[box_index++].push_back(stoi(n_constructor));
            n_constructor = "";
        }
    }
    (*new_box_list.boxes) = n_vector;
    return new_box_list;
}

int main(int argc, char* argsv[])
{
    char* command_string = argsv[0];
    string file_name = argsv[1];
    //
    int epochs = 10;
    int tabu_length = 2;
    //
    int weight, item_amount;
    BoxList initial_sol = bin_pack_from_file(file_name, weight, item_amount);
    Solutions solutions;
    solutions.global_solution = initial_sol;
    solutions.local_solution = initial_sol;
    // get neighbors, local search for each, check fitness, if higher than local, then it is the current local
    // also global if necessary
    for (int i = 0; i < epochs; i++)
    {
        vector<BoxList> neighbors = create_neighbors(initial_sol);
        solutions.local_solution = neighbors[0];
        for (BoxList box_list : neighbors)
        {
            local_search(box_list);
            int fitness = box_list.get_fitness();
            if (fitness > solutions.local_solution.get_fitness() && !solutions.has_on_tabu(box_list))
            {
                solutions.local_solution = box_list;
            }
            if (fitness > solutions.local_solution.get_fitness())
            {
                solutions.global_solution = box_list;
            }
        }
        if (solutions.tabu_list.size() == tabu_length) solutions.tabu_list.erase(solutions.tabu_list.begin());
        solutions.tabu_list.push_back(solutions.local_solution);
        
    }
    return 0;
}
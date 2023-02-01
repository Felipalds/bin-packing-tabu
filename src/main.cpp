#include "boxstructure.h"
#include "binpack.h"
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

BoxList bin_pack_from_file(
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

    int weight, item_amount;
    BoxList box_list = bin_pack_from_file(file_name, weight, item_amount);
    cout << weight << '\n' << item_amount << '\n';
    for (vector<int> v : (*box_list.boxes))
    {
        cout << v[0] << '\t';
    }

    return 0;
}
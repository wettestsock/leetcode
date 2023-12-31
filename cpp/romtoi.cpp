#include <iostream>
#include <forward_list>
#define N '\n'
/*
ROMAN INTEGER TO NUMBER

if curr < next then substract
if curr > next then add

g++ romtoi.cpp -o out\romtoi
out\romtoi

g++ romtoi.cpp -o linout/romtoi
linout/romtoi

*/
unsigned short int rom_to_num(const char& rom_input){
        switch(rom_input){
            case 'I':   return 1;       break;
            case 'V':   return 5;       break;
            case 'X':   return 10;      break;
            case 'L':   return 50;      break;
            case 'C':   return 100;     break;
            case 'D':   return 500;     break;
            case 'M':   return 1000;    break;
            default:    return 0;
        }
};

class Solution{
    public:
    static unsigned int rom_to_int(const std::string& input){
        unsigned int result = 0;
        for(int i=0; i<input.length(); ++i){
            unsigned short int curr = rom_to_num(input[i]);
            if(i+1 < input.length() && curr < rom_to_num(input[i+1])) { 
                //if it's NOT the last char and next is bigger
                result -= curr;
            } else {
                //if next is smaller
                result += curr;
            }
        }
        return result;
    }
};  


//operator overloading for forward lists 
template<typename T>
std::ostream& operator<<(std::ostream& output, const std::forward_list<T>& list){
    for(const T& i : list) output<< i;

    return output;

};

int main(){
    //returns 998
    std::cout << Solution::rom_to_int("CMXCVIII")<<N;
    std::forward_list<char> roman_nums;
    roman_nums.assign({'C','M','X','C','V','I','I','I'});
    std::forward_list<int> test;
    test.assign(5,3); //5 elements each of 3
    test.assign(6,2); // reassigns the linked list
    std::cout <<test << N; 
    std::cout<<roman_nums;


};
#include <string>
#include <iostream>
bool solution(std::string S) {
    // write your code in C++14 (g++ 6.2.0)
    bool b_found=false;
    bool ret=true;
    for(const char& letter : S){
        if(letter=='a' && b_found==true){
            std::cout<< "1: "<<letter<<std::endl;
            return false;
        }else{
            std::cout<< "2: "<<letter<<std::endl;
            if(letter=='b'){
                std::cout<< "3: "<<letter<<std::endl;
                b_found=true;   
            }
        }
    }
    return ret;
}

int main(){
    std::string st{"abba"};
    bool res=solution(st);
    std::cout<<"result: "<<res<<std::endl;
}
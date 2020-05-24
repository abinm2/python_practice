// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <algorithm>
using namespace std;
vector<int> solution(vector<int> &A, int Y) {
    // write your code in C++14 (g++ 6.2.0)
    vector<int> ret{};
    int prev_sum=0;
    int i;
    for(i=A.size()-1;i>=0;i--){
        A[i]=prev_sum+A[i];
        prev_sum= A[i];
    }
    for(i=0;i<=A.size()-1-Y;i++){
        A[i]=A[i]-A[i+Y];
    }
    auto max1=std::max_element(A.begin(),A.end());
    int tot_org=*max1;
    int index1=std::distance(A.begin(),max1);
    for(i=index1;i<=index1+Y-1;i++){
        A[i]=-1;
    }
    A[index1]=-1;
    auto max2=std::max_element(A.begin(),A.end());
    tot_org+=*max2;
    int index2=std::distance(A.begin(),max2);
    if(index1<index2){
        ret.push_back(index1);
        ret.push_back(index2);
    }else{
        ret.push_back(index2);
        ret.push_back(index1);
    }
    ret.push_back(tot_org);
    return ret;
}
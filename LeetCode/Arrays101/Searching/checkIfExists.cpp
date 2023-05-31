#include <vector>
#include <iostream>

class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
                

    // Basic solution: nested loop
        for(int i=0;i<arr.size();i++){
            // i will be i in the problem

            // Below is the nested loop, we will check all our rules in this loop
            for(int j=0;j<arr.size();j++){
                // 1. i!=j
                if(i!=j){ // Code will not run if i==j
                    // 2. 0 <= i, j < arr.length
                    // Our loop constraints will make sure that this condition is met

                    // if arr[i] == 2 * arr[j] return true
                    if(arr[i]==2*arr[j]){
                        return true; 
                    }
                } 

            }

        }  
    }
};
#include <iostream>
#include <vector>


using namespace std;
bool checkIfExist(vector<int>& arr);
// This is used for testing my code 
int main(){
    vector<int> array = {10,2,5,3};

    cout << checkIfExist(array) << endl;
} 

bool checkIfExist(vector<int>& arr) {
    
    for(int i=0;i<arr.size()-1;i++){
        for(int k=i+1;k<arr.size();k++){
            if(i!=k) // Make sure they aren't the same index
            {
                // Given Conditions
                if(0<=i&&k<arr.size()){
                    if(arr[i]==2*arr[k]){
                        return true;
                    }
                }

                // Instead of having the interior loop start from the begininng, we can just swap i and k!
                if(0<=k&&i<arr.size()){
                    if(arr[k]==2*arr[i]){
                        return true;
                    }
                }


            }
        }
    }
        
}

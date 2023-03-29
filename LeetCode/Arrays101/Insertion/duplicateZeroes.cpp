#include <iostream>
#include <vector>

using namespace std;

// DIRECTIONS: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

// Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

// Solution: O(N) Shift on each 0 via forloop
class Solution {
public:
    void duplicateZeros(vector<int>& arr) 
    {

        // My first solution was pretty slow, lets change that
        vector<int> newArr;
        int n = arr.size();
        for(int i=0;i<n;i++)
        {
            newArr.push_back(arr[i]);
            if(arr[i]==0)
            {
                n=n-1;  
                newArr.push_back(arr[i]); // Places a second 0 into the new array, and decrements N, which will effectively cut a higher index out
            }
        }
        if(arr.size()<newArr.size()){
            newArr.pop_back();
        }

        // Old Solution
        for(int i=0;i<arr.size();i++)
            {
                if(arr[i]==0) // Check if the current index is equal to 0, if it is, begin shifting
                {
                    for(int k=arr.size()-1;k>i;k--) // For loop from 1 index past the 0
                    {
                        arr[k] = arr[k-1];
                    }
                    // Now we should have an array with the 0 doubled at this location
                    for(int x=0;x<arr.size();x++){
                        cout << arr[x] << " ";
                    }
                    cout << endl;
                    i++; // Incrementing this i will ensure that the loop does not try to double the new 0 that was just inputted
                }
            }

        // Setting final value equal
        arr = newArr;
    }   
};
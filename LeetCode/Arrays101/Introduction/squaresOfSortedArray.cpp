#include <iostream>
#include <vector>

using namespace std;
/*
DIRECTIONS: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 
*/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) 
    {
        vector<int> squaredVector;

        for(int i=0;i<nums.size();i++)
        {
            int square = nums[i]*nums[i]; // Square the number
            
            squaredVector.push_back(square); // Add the square to the end of the array
        }

        // Now we just need to sort the new array

        // Let's use counting sort
        // For counting sort, we first need to find the maximum value in the array, and put every value into the array
        vector<int> countingSort;
        int max = 0;
        for(int k=0;k<squaredVector.size();k++)
        {
            if(squaredVector[k]>max){max=squaredVector[k];}
            countingSort[squaredVector[k]]++;
        }
        // Now lets resize to max+1
        countingSort.resize(max+1);
        for(int z=0;z<countingSort.size();z++){
            cout << countingSort[z] << " ";
        }
    }
};

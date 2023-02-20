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
        /* Debug Printing
        cout << "Printing squared array" << endl;
        for(int i=0;i<squaredVector.size();i++)
        {
            cout << squaredVector[i] << " ";
        }
        */

        // Now we just need to sort the new array

        // Let's use counting sort
        // For counting sort, we first need to find the maximum value in the array, and put every value into the array
        vector<int> countingSort;
        int max = 0;

        for(int k=0;k<squaredVector.size();k++)
        {
            if(squaredVector[k]>max){max=squaredVector[k];}
        }
        // Now lets resize to max+1
        countingSort.resize(max+1);
        for(int z=0;z<squaredVector.size();z++){
            int temp = squaredVector[z];
            countingSort[temp]++;
        }

        /* Print Debugging
         cout << "\nPrinting counted array" << endl; 
        for(int i=0;i<countingSort.size();i++)
        {
            cout << countingSort[i] << " ";
        }
        cout << endl;
        */

      /*  Made this too complicated
        int cumSum = 0; // Cumulative Sum
        for(int xx=0;xx<countingSort.size();xx++){
            int temp = countingSort[xx];
            countingSort[xx]+=cumSum;
            cumSum+=temp;
        }
     */

        vector<int>output;
        int outputIterator = 0; // Use this variable to iterate through the output array and assign values - NOT USED 
        for(int xx=0;xx<countingSort.size();xx++)
        {
            while(countingSort[xx]>0)
            {
                output.push_back(xx);
               // cout << "Pushing " << xx << " to back of array" << endl;
                countingSort[xx]--;
            }
        }

        return output;
    }
};

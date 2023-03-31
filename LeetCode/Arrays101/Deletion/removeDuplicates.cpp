#include <iostream>
#include <vector>


// This solution was in the top 5% in terms of speed
class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) 
    {

        int s = nums.size();

        int yes = 0;
        if(s==0){return 0;} // If the vector is empty element, return 
        if(s==1){return 1;} // If the vector is only 1 element, return 1

        // Otherwise, we can loop through the vector
        for(int i=0;i<s;i++)
        {  
            // If the currentIndex is 1 below the size, add it to the final array and then return to avoid errors
            if(i+1==s){
                nums[yes] = nums[i];
                yes++;
                return yes;
            }

            if(nums[i]==nums[i+1]) // if the value of currentIndex is equal to the value of the next index
            {
                int iterator = i+1; // Set an iterator

                while(iterator<s&&nums[i]==nums[iterator]) // Loop until a value is found that is not the same as nums[i] or until the iterator has reached the max
                {
                    iterator++;
                }
                nums[yes] = nums[i]; // Then put nums[i] at the correct location in the reduced array
                i=iterator-1; // Set i to the new iterator location and reduce it by 1 (It'll get one added to it by the for loop)
                yes++; // Increment the size of the reduced array
            } else {
                nums[yes] = nums[i];
                yes++;
            }
        }
        return yes;
    }
};
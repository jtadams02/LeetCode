#include <iostream>
#include <vector>


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        /* This solution works, but its not the most efficient. This causes us to loop over the array everytime, could be bad on a large dataset
        i'll make a better solution
        int kCount = 0; // This will be our counter that we return
        // int vectorSize = nums.size();
        
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i] == val){ 
                // If the current index of nums is equal to the val number
                // Lets try to remove it

            // int temp = nums[i]; // Set temp variable? Not needed

                for(int k=i+1;k<nums.size();k++){ // Use this loop to move every index up
                    nums[k-1] = nums[k]; // this sets index k-1 equal to k, or it sets the previous index to the current index. This shifts everything to the left.
                }
                nums.pop_back(); // Remove the last index of the vector, which will just be a duplicate of the second to last index, we need to pop it
                i--; // Decrease i so that the index remains at the same place, this is so we can check if the new value we just moved into i is equal to val
            } else {
                kCount++; // Increment size of the array without val
            }
        }

        return kCount; // Return how many elements are in the subtracted array!
        */


       // This solution is much more efficient, it only takes O(n) compared to my above solution which wasn't too slow, but on a very large array it may have taken a lot longer
       // than what this would take on a very large array
       int k = 0;
       for(int i=0;i<nums.size();i++)
       {
            if(nums[i]!=val) // If the currentIndex does NOT equal the value to remove
            {
                nums[k] = nums[i]; // Put the allowed value into the array
                k++; // Increment the new array size coutner
            }
       }
       return k;
    }
};
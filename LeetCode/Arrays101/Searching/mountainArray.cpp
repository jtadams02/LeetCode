
#include <vector> 
#include <iostream>

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        

        // A mountain array is an array that increases to a certain point, then decreases after that point 

        // My attempted solution will be to loop through the array with certain if statements executing at a certain point

        /* Constraints for mountain array
        *  arr.length >= 3 
        * There exists some i with 0 < i < arr.length - 1 such that:
        *  arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        *  arr[i] > arr[i + 1] > ... > arr[arr.length - 1
        */

       // SOLUTION 2: Let's try to be quicker

        // First off, if the array is smaller than 3 then it is invalid
        if(arr.size()<3){
            return false;
        } else {
            // Otherwise we need to check and make sure that this is a valid array

            // Edge case where size = 3?
            if(arr.size()==3){
                if(arr[0]<arr[1]&&arr[1]>arr[2]){
                    return true;
                } else {
                    return false;
                }
            }
            bool increased = false;
            // When size > 3
            // To do so, we need to loop through the array. Runtime of this will be O(N) if done properly
            for(int i=1;i<arr.size();i++){
                
                // Edge case when doubled
                if(arr[i]==arr[i-1]){return false;}

                if(arr[i]>arr[i-1]){
                    // This code will run when the array is increasing at this index
                    // At the start, it should always be increasing
                    increased = true;
                } else {
                    // Now if arr[i] < arr[i-1], we're going to assume we're decreasing now
                    
                    // From here I am going to implement a new for loop
                    // This for loop will check only for decreasing values
                    for(int j=i;j<arr.size();j++){
                        if(arr[j]<arr[j-1]){
                            // If the current index has a value less than the previous index this code will run 
                        } else {
                            return false;
                        }
                    }
                    // At this point we should be at the end of the array with no returns. This will only return if the increasing code breaks, and then the decreasing never stops
                    if(increased){
                        return true;
                    }
                }
            }
            return false;
        }

       // BELOW IS SOLUTION 1: SOLUTION 1 IS A VERY SLOW SOLUTION 

        // Mountain arrays must be >= 3, so if its less than 3 return false 
        if(arr.size()<3){
            return false;
        } else {
            // Declare variable to let us know whether it should be increasing or decreasing
            bool increase = true;
            // These two below variables will help me track whether or not the array has gone up and gone down
            bool didIncrease = false;
            bool didDecrease = false;
            for(int i=1;i<arr.size();i++){
                // Otherwise, we go into the loop

                // I think we can just simplify this, if there is a repeat value we can just return false
                if(arr[i]==arr[i-1]){
                    return false;
                }

                // if increase = true, make sure we're increasing 
                if(increase){
                    if(arr[i] <= arr[i-1]){
                        // If i is less than its predecessor, we need to start checking decreasing
                        increase = !increase;
                    } else {
                        // Otherwise, we have increased
                        didIncrease = true;
                    }
                } 
                
                if(!increase) {
                    // Now we're assuming that we're going down the mountain
                    if(arr[i] >= arr[i-1]){
                        // If i is more than its predecessor then the mountain is not valid 
                        return false;
                    }
                    // otherwise, we have decreased
                    didDecrease = true;
                }
            }
            // If the array hasn't decreased or increased, it cannot be a valid mountain array
            if(didIncrease&&didDecrease){
                return true;
            }
            return false;
        }
    }
};
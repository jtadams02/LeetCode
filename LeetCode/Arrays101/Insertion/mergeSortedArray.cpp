#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // This function will merge the two sorted arrays. O(n+m) runtime in any situation
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

         // Setup variables, use itN to track iterations through the arrays
        int it1 = 0;
        int it2 = 0;
        
        vector<int> newVect;

        while(1)
        {
            // Check if any of the arrays have reached their limits?
            if(it1>=m&&it2>=n){break;} // If bother array iterators are > then their size, then the while loop should break
                if(it1>=m) // This if statement checks if nums1 iterator has reached the supposed max value of the array
                {
                    // If all the values of num1 have already been used, then we just push back whatever is left from nums2[it2]
                    newVect.push_back(nums2[it2]);
                    it2++;
                    continue; // Loop over
                }
                if(it2>=n) // Is nums2 iterator greater than the max value of nums2
                {
                    newVect.push_back(nums1[it1]);
                    it1++;
                    continue;
                }

            if(nums1[it1]<nums2[it2]){ // If nums1[currentIndex] < nums2[currentIndex2] then add the lowest value to the new array!

                cout << nums1[it1] << " < " << nums2[it2] << endl;
                newVect.push_back(nums1[it1]);
                it1++; // Increment that thang cuzzo

            } else if(nums1[it1]==nums2[it2]) // wha happens when the values are equal?
            {
                // When the values are equal we're just going to take from both and increment both
                cout << nums1[it1] << " = " << nums2[it2] << endl;
                newVect.push_back(nums1[it1]);
                it1++;
                newVect.push_back(nums2[it2]);
                it2++;
            } else { 
                // ELSE we can infer that since nums1[it1] is not less than or equal to nums2[it2] then nums2[it2] must be less than nums1[it1]
                cout << nums1[it1] << " > " << nums2[it2] << endl;
                newVect.push_back(nums2[it2]);
                it2++;
            }
        }


        nums1 = newVect;
    }
};
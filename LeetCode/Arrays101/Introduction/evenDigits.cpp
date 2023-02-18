#include <iostream>
#include <vector>

using namespace std;
/*
DIRECTIONS: Given an array nums of integers, return how many of them contain an even number of digits.
*/
class Solution {
public:

    int findNumbers(vector<int>& nums) 
    {
        int maxDigits=0;
        for(int i=0;i<nums.size();i++)
        {
            int digits=0;
            int digit = nums[i];
            do{
                digit/=10;
                digits++;
            } while(digit!=0);

            if(digits%2==0){maxDigits++;}
        }
        return maxDigits;
    }

};
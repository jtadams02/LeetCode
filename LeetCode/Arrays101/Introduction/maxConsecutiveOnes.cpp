#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    Solution()
    {
        for(int i=0;i<10;i++)
        {
            numbers.push_back(rand()%2);
        }
        size = 10;
    }
    Solution(int k)
    {
        for(int i=0;i<k;k++)
        {
            numbers.push_back(rand()%k);
        }
        size = k;
    }   
    int findMaxConsecutiveOnes(vector<int>& nums) 
    {

        bool oneFound = false;
        int maxCount = 0;
        int tempCount = 0;

        for(int i=0;i<=nums.size();i++)
        {
            if(nums[i]==1) // If the value is 1, begin 1-sequencing, adding to tempCount everytime
            {
                if(oneFound==false)
                {
                    oneFound=true;
                }
                tempCount++;
            }else // Value is a 0
            {
                if(oneFound) // Check if there was a sequence of ones before this 0
                {
                    oneFound=false;
                    // Now we compare max count, set the max to temp, and reset the temp
                    if(tempCount>maxCount)
                    {

                        maxCount=tempCount;
                        /* IGNORE THIS
                        // If the one count is only equal to 1, we ignore it because it is not a 1 sequence
                        if(tempCount==1){
                            maxCount=maxCount;
                        }else {maxCount=tempCount;}
                        */
                    }
                    tempCount=0;
                }
            }
        }
        // There's a chance that the last sequence of numbers can contain a series of 1's, which the for loop
        // Will not compare to the max count, so we compare that here and now

            if(tempCount>maxCount){maxCount=tempCount;} // Set the maxCount = tempCount 
        return maxCount;
    }
    vector<int> returnVectoid()
    {
        return numbers;
    }
    void print()
    {
        for(int i=0;i<size;i++)
        {
            cout << numbers[i] << " ";
        }
    }

private: 
    vector<int> numbers;
    int size;
};

int main()
{
    Solution *n =  new Solution();
    n->print();
    cout << n->findMaxConsecutiveOnes(n->returnVectoid()) << endl;
}
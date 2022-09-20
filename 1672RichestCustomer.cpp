#include <vector>
class Solution {
public:
    int maximumWealth((vector<vector<int>>)& accounts) 
    {
       int maxSum = 0;
       int maxCust = 0;
        for(int i=0;i<accounts.size();i++)
        {
            int tempSum = 0;
            for(int k=0;k<accounts.at(i).size();k++)
            {
                tempSum+=accounts.at(i).at(k);
            }
            if(tempSum>maxSum)
            {
                maxCust = i;
                maxSum = tempSum;
            }
        }
        return maxSum;
    }
};
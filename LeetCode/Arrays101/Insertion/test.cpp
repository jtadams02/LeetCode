#include <iostream>
#include <vector>

using namespace std;
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n);
int main()
{
    int m,n;
    m = 3;
    n = 3;
    vector<int> nums1(m+n);
    vector<int> nums2(n);
    nums1[0] = 1;
    nums1[1] = 2;
    nums1[2] = 3;
    nums2[0] = 2;
    nums2[1] = 5;
    nums2[2] = 6;
    
    merge(nums1,m,nums2,n);

    for(int i=0;i<nums1.size();i++)
    {
        cout << nums1[i] << " ";
    }
    




}

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
{
        // Setup variables, use itN to track iterations through the arrays
        int it1 = 0;
        int it2 = 0;
        vector<int> newArr;

        while(it2<nums2.size())
        {
            
        }

        nums1 = newArr;
}
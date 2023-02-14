#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'kSub' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY nums
 */

long kSub(int k, vector<int> nums) 
{
    long endLong = 0;
    for(int i=0;i<nums.size()-1;i++)
    {
        int selectedNum = nums.at(i);
        if(selectedNum%k==0){endLong++;}
        vector<int> tempVector;
        tempVector.push_back(nums.at(i));
        for(int k=i+1;k<nums.size();k++)
        {
            int tempSum = 0;
            tempVector.push_back(nums.at(k));
            for(int j=0;j<tempVector.size();j++)
            {
                tempSum = tempSum + tempVector.at(j);
                cout << tempSum << endl;
            }
            if(tempSum%k==0){endLong++;}
        }
    }
    return endLong;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string k_temp;
    getline(cin, k_temp);

    int k = stoi(ltrim(rtrim(k_temp)));

    string nums_count_temp;
    getline(cin, nums_count_temp);

    int nums_count = stoi(ltrim(rtrim(nums_count_temp)));

    vector<int> nums(nums_count);

    for (int i = 0; i < nums_count; i++) {
        string nums_item_temp;
        getline(cin, nums_item_temp);

        int nums_item = stoi(ltrim(rtrim(nums_item_temp)));

        nums[i] = nums_item;
    }

    long result = kSub(k, nums);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

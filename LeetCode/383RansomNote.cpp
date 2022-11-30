#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool canConstruct(string ransomNote, string magazine);
struct LinkedList
{
    
};
int main()
{
    string ransom,maga;
    /* cout << "Enter the word you want to match: ";
    cin >> ransom;

    cout << "Enter the characters you want to use to create the match: ";
    cin >> maga; */
    ransom = "fffbfg";
    maga = "effjfggbffjdgbjjhhdegh";

    cout << "\n" << canConstruct(ransom,maga);
}

bool canConstruct(string ransomNote, string magazine) 
{
    // Solution without Hashmap
    // This Solution Works, but is slower than 80% of LeetCode, how do we make it faster?
    /*
                if(ransomNote.size()>magazine.size()){return false;}
    vector<char> mag;

    for(int i=0;i<magazine.size();i++)
    {
        mag.push_back(magazine[i]);
    }

    for(int i=0;i<ransomNote.size();i++)
    {
        bool isCharThere = false;
       // for(char w: mag){cout<<w;}
      //  cout << " || To Match With: " << ransomNote[i];
        vector<char>::iterator it = mag.begin();
        for(it;it<mag.end();it++)
        {
            if(*it==ransomNote[i])
            {
                mag.erase(it);
                isCharThere=true;
                break;
            }
        }   
        if(!isCharThere){return false;}
        //cout << endl;
    }
    return true;
    */


    // Solution with a HashMap
        


}
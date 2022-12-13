#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<string> split(string input);
char findExtraCharcter(string strA, string strB);
int conversion(char x, vector<char> alpha);
int getIndex(vector<char> v, char K);
char findDoubleChar(string one, string two);
char findTripleChar(string one, string two, string three);
bool findThirdChar(char m, string one);

int main(int argc, char* argv[])
{
    // I imagine the best solution for this is to read a file input, so lets set that up
    ifstream myFile;
    if(argc!=2){cout<<"You have the incorrect amount of arguments!";return -1;}
    string fileName = argv[1];
    myFile.open(fileName);

    // We need another input variable
    string input;

    // Initialize alphabet vector
    vector<char> alpha{'-'};
    char init = 'a';
    char initU = 'A';
    for(int i=0;i<26;i++)
    {
        alpha.push_back((char)(init+i));
    }
    for(int i=0;i<26;i++)
    {
        alpha.push_back((char)(initU+i));
    }
    
    // Counter variable
    int counter =0;
    // Now, lets get that input 
    int count = 0;
    int firstTwo = 0;
    vector<string> tres;
    while(getline(myFile,input))
    {
        string why = input;
        tres.push_back(why);
        cout << tres[count] << endl;
        count++;
    }

    /*
    string one = tres[0];
    string two = tres[1];
    string three = tres[2];

    cout << "1:" << one <<"\n2:" << two << "\n3:" << three << endl;

    cout << "\nLets find the matching character in all three!" << endl;

    for(char x : one)
    {
        for(char y : two)
        {
            if(x==y){
                if(isspace(y)){break;}
                cout << y << " is in both one and two, lets see if it is in three" << endl;
                for(char z : three)
                {
                    if(z==y)
                    {
                        cout << "The matching string for all 3 is: " << z << endl;
                    }
                }
            }
        }
    } */


    for(int i=0;i<tres.size();i+=3)
    {   
        char m1 = findTripleChar(tres[i],tres[i+1],tres[i+2]);

        if(m1!='-')
        {
            counter += conversion(m1,alpha);
            cout << tres[i] << endl;
            cout << tres[i+1] << endl;
            cout << tres[i+2] << endl;
            cout << "\nThe Matching char is: " << m1 << endl;
            cout << endl;

        } else {cout << "No match for these 3" << endl;}

    }

    cout << counter << endl;
    cout << count << endl;

}
// Used for testing, copied from https://www.geeksforgeeks.org/how-to-find-index-of-a-given-element-in-a-vector-in-cpp/
// NVM we need this lol
int getIndex(vector<char> v, char K)
{
    auto it = find(v.begin(), v.end(), K);
  
    // If element was found
    if (it != v.end()) 
    {
      
        // calculating the index
        // of K
        int index = it - v.begin();
        return index;
    }
    else {
        // If the element is not
        // present in the vector
        return -1;
    }
}

// Gets the numerical value for the character
// My own solution, probably bad
int conversion(char x, vector<char> alpha)
{

    return getIndex(alpha,x);
}

// Splits strings in half
vector<string> split(string input)
{
    // Get the index of the center of the string
    int half = input.size()/2;

    // Now lets create two substrings, which create two strings split down the middle of the old one
    string firstHalf = input.substr(0,half);
    string lastHalf = input.substr(half);

    // Add to vector and return!
    vector<string> returnVectoid;
    returnVectoid.push_back(firstHalf);
    returnVectoid.push_back(lastHalf);

    return returnVectoid;
}

char findDoubleChar(string one, string two)
{
    // This solution is O(n^2) but my hashmap isnt working
    // I'll fix it later lol
    char matchingChar='-';
    for(int x=0;x<one.size();x++)
    {   
        char tempChar = one[x];
        for(int k=0;k<two.size();k++)
        {
            if(tempChar==two[k]){
                matchingChar = tempChar;
            }
        }
    }

    return matchingChar;

}

char findTripleChar(string one, string two, string three) 
{
    char matchingChar='-';
    for(char x : one)
    {
        if(isspace(x)){continue;}
        for(char y : two)
        {   
            if(x==y)
            {
                for(char z : three)
                {
                    if(y==z)
                    {
                        matchingChar = z;

                    }
                }
            }
        }
    }
    
    return matchingChar;
}

bool findThirdChar(char m, string one)
{
    for(char x : one)
    {
        if(x==m)
        {
            return true;
        }
    }
    return false;
}
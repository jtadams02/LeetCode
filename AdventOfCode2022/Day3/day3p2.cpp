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
       // cout << (char)(init+i) << ", at index: " << getIndex(alpha,((char)(init+i))) << endl;
    }
    for(int i=0;i<26;i++)
    {
        alpha.push_back((char)(initU+i));
       // cout << (char)(initU+i) << ", at index: " << getIndex(alpha,((char)(initU+i))) << endl;
    }
    
    // Counter variable
    int counter =0;
    // Now, lets get that input 
    int count = 0;
    int firstTwo = 0;
    vector<string> tres;
    while(getline(myFile,input))
    {
        
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
    for(int x=0;x<one.size();x++)
    {   
        char tempChar = one[x];
        for(int k=0;k<two.size();k++)
        {
            if(tempChar==two[k]&&tempChar==three[k]){
                matchingChar = tempChar;
            }
        }
    }

    return matchingChar;
}
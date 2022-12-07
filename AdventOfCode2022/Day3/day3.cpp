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
    while(getline(myFile,input))
    {
        // Now we need to split the string
        vector<string> splitted = split(input);

        // Now we have a vector with the string split in half
        // We must compare the two strings and find the one that exists in both
        // What is the best way to implement this? 
        // HASH MAP

        // This char will be the character found in both
        char match = findDoubleChar(splitted.at(0),splitted.at(1));
        cout << "The double char is \'" << match << "\'";

        // Now we need to convert that to a numerical value
        // lowercase is 1-26, uppercase 27-52

        int numValue = conversion(match,alpha);
        cout << ". Its value is: " << numValue;
        counter += numValue;
        cout << ", and the running total is: " << counter << endl;

    }

    cout << counter;
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

// Hashmap function to find matching char
char findExtraCharcter(string strA, string strB)
{
    //O(n) ! ! ! 
    // store string values in map
    unordered_map<char, int> m1;
 
    // store second string in map with frequency
    for (int i = 0; i < strB.length(); i++)
        m1[strB[i]]++;
 
    // store first string in map with frequency
    for (int i = 0; i < strA.length(); i++)
        m1[strA[i]]--;
 
    for (auto h1 = m1.begin(); h1 != m1.end(); h1++) {
 
        // if the frequency is 1 then this
        // character is which is added extra
        if (h1->second == 1)
            return h1->first;
    }
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
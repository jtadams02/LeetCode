#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    // I imagine the best solution for this is to read a file input, so lets set that up
    ifstream myFile;
    if(argc!=2){cout<<"You have the incorrect amount of arguments!";return -1;}
    string fileName = argv[1];
    myFile.open(fileName);

    string input; 

    while(getline(myFile,input))
    {   
        vector<string> result;
        stringstream s_stream(input); //create string stream from the string
        while(s_stream.good()) {
            string substr;
            getline(s_stream, substr, ','); //get first string delimited by comma
            result.push_back(substr);
        }
        
        // Now we need to find which range is bigger
        
    }


}
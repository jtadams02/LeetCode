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
    vector<string> x{"Test","Test2","Test3","Test4"};
    for(auto k : x){
        cout << k << " ";
    }
    char input;
    cout << "Input a char: " << endl;
    cin >> input;

    cout << "You've selected: " << input << "\nChar+1 = " << (char)(input+1) << endl;
}
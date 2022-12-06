#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <ctype.h>

using namespace std;

int main(int argc, char* argv[])
{
    // We're back for day 2, and we gotta read our input so lets set it up!
    ifstream myFile;
    if(argc!=2){cout<<"You have the incorrect amount of arguments!";return -1;}
    string fileName = argv[1];
    myFile.open(fileName);
    
    // Since we are reading from a file, I want to use getline. Getline cannot use ints (I think) so we use a string
    string input;

    int score = 0;
    // Now lets loop through until EOF (End of File)
    while(getline(myFile,input))
    {
        // Just in case, we break when there isnt an alphabetical character detected
        if(!isalpha(input.at(0))){break;}
        // Declare our variables, first is the first column, last is the second column
        char first = input.at(0);
        char last = input.at(2);

        // Convert for ease of mind
        // Scoring: A=1,B=2,C=3
        if(last=='X'){last='A';}
        if(last=='Y'){last='B';}
        if(last=='Z'){last='C';}

        // A hashmap would be easier to use but i dont feel like doing that yet
        // So we're gonna do each possibility

        // When our pick is A
        if(last=='A') 
        {
            // No matter what, score is always increased one
            score+=1;

            // When A==A, or when it is a draw
            if(last==first)
            {
                score+=3;
            }
            // When A==B, or when it is a loss
            if(first=='B')
            {
                // Loss, nothing happens
            }

            // When A==C, or when it is a win
            if(first=='C')
            {
                score+=6;
            }
        }
        // When our pick is B
        if(last=='B') 
        {
            // No matter what, score is always increased one
            score+=2;

            // When B==B, or when it is a draw
            if(last==first)
            {
                score+=3;
            }
            // When B==A, or when it is a win
            if(first=='A')
            {
                score+=6;
            }

            // When B==C, or when it is a loss
            if(first=='C')
            {
                // Loss, nothing happens
            }
        }
        // When our pick is C
        if(last=='C') 
        {
            // No matter what, score is always increased one
            score+=3;

            // When C==C, or when it is a draw
            if(last==first)
            {
                score+=3;
            }
            // When C==B, or when it is a win
            if(first=='B')
            {
                score+=6;

            }

            // When C==A, or when it is a win
            if(first=='C')
            {
                // Loss, nothing happens
            }
        }
        cout << score << endl;
    }
}
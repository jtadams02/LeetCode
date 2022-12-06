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
        // X=loss,Y=draw,Z=win
        // A=rock, B=paper, Z=scissors

        // A hashmap would be easier to use but i dont feel like doing that yet
        // So we're gonna do each possibility

        // We need to lose
        if(last=='X')
        {
            // No score added for losing
            // When the opponent chooses A, we need to pick C
            if(first=='A')
            {
                // Add 3 for choosing C
                score+=3;
            }
            // When the opponent chooses B, we need to pick B
            if(first=='B')
            {
                // Add 1 for choosing A
                score+=1;
            }
            // When the opponent chooses C, we need to pick B
            if(first=='C')
            {
                // Add 2 for choosing B
                score+=2;
            }
        }
        // We need to draw
        if(last=='Y')
        {
            // Under the assumption we always draw
            score+=3;
            // When the opponent chooses A, we need to pick A
            if(first=='A')
            {
                // Add 1 for choosing A
                score+=1;
            }
            // When the opponent chooses B, we need to pick B
            if(first=='B')
            {
                // Add 2 for choosing B
                score+=2;
            }
            // When the opponent chooses C, we need to pick C
            if(first=='C')
            {
                // Add 3 for choosing C
                score+=3;
            }

        }

        // We need to win
        if(last=='Z')
        {
            // Under the assumption that we always win
            score+=6;

            // When the opponent chooses A, we need to pick B
            if(first=='A')
            {
                // Add 2 for choosing B
                score+=2;
            }
            // When the opponent chooses B, we need to pick C
            if(first=='B')
            {
                score+=3;
            }
            // When the opponent chooses C, we need to pick A
            if(first=='C')
            {
                score+=1;
            }
        }
        cout << score << endl;
    }
}
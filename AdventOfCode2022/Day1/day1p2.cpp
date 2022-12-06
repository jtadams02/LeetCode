#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <ctype.h>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    // I imagine the best solution for this is to read a file input, so lets set that up
    ifstream myFile;
    if(argc!=2){cout<<"You have the incorrect amount of arguments!";return -1;}
    string fileName = argv[1];
    myFile.open(fileName);
    
    // Lets create our variables, we need 3 maxes
    int absoluteMax = 0;
    int midMax = 0;
    int minMax = 0;
    vector<int> counts;
    counts.push_back(0);
    counts.push_back(0);
    counts.push_back(0);
    

    int countMax,countMid,countMin = 0;
    
    // Since we are reading from a file, I want to use getline. Getline cannot use ints (I think) so we use a string
    string input;

    // Now lets loop through until EOF (End of File)
    int count = 0;
    while(!myFile.eof())
    {   
        // Initialize our counter we will use for this group of ints of the file
        int currentCount = 0;

        //cout << "Elf #" << count << endl;
        // This will loop until the end of the file, now we want to loop until we hit a empty line
        while(getline(myFile,input))
        {
            // This will break the loop and start a new one on empty line
           // cout << "Checking input: " << input << ". It's size is: " << input.size() << endl;

           if(!isdigit(input[0]))
            {
                //cout << "New Elf Now" << endl;
                break;
            } else {
                // Now convert the string from getLine to our counter
                int temp = stoi(input);
                currentCount = currentCount + temp;
            }
           // cout << "The current count is: " << currentCount << endl;
        }
            // Now we check if its the maximum amount, if it is, set maxCount = currentCount
            cout << "Elf #" << count << ", is carrying " << currentCount << " calories" << endl;
            if(currentCount>=counts.at(0))
            {
                counts.insert(counts.begin(),currentCount);
                count++;
            } else if(currentCount>=counts.at(1))
            {
                counts.insert(counts.begin()+1,currentCount);
                count++;
            } else if(currentCount>=counts.at(2))
            {
                counts.insert(counts.begin()+2,currentCount);
                count++;
            } else {
                count++;
            }

          /*  if(currentCount>=absoluteMax)
            {
                midMax = absoluteMax;
                absoluteMax = currentCount;
                count++;
            } else if(currentCount>=midMax)
            {
                minMax = midMax;
                midMax = currentCount;
                count++;
            } else if(currentCount>=minMax){
                minMax = currentCount;
                count++;
            } else {
                count++;
            }*/
    }
    cout<<"1: "<<counts.at(0) <<"\n2: "<<counts.at(1) <<"\n3: "<<counts.at(2) <<endl;
    cout << "Total: " << counts.at(0) +counts.at(1) +counts.at(2) ;
}
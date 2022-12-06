#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <ctype.h>

using namespace std;

int main(int argc, char* argv[])
{
    // I imagine the best solution for this is to read a file input, so lets set that up
    ifstream myFile;
    if(argc!=2){cout<<"You have the incorrect amount of arguments!";return -1;}
    string fileName = argv[1];
    myFile.open(fileName);
    
    // Lets create our variable
    int maxCount = 0;
    
    // Since we are reading from a file, I want to use getline. Getline cannot use ints (I think) so we use a string
    string input;

    // Now lets loop through until EOF (End of File)
    while(!myFile.eof())
    {   
        // Initialize our counter we will use for this group of ints of the file
        int currentCount = 0;
        int count = 0;
        cout << "Elf #" << count << endl;
        // This will loop until the end of the file, now we want to loop until we hit a empty line
        while(getline(myFile,input))
        {
            // This will break the loop and start a new one on empty line
            cout << "Checking input: " << input << ". It's size is: " << input.size() << endl;

           if(!isdigit(input[0]))
            {
                cout << "New Elf Now" << endl;
                break;
            } else {
                // Now convert the string from getLine to our counter
                int temp = stoi(input);
                currentCount = currentCount + temp;
            }
            cout << "The current count is: " << currentCount << endl;
        }
            // Now we check if its the maximum amount, if it is, set maxCount = currentCount
        if(currentCount>maxCount)
        {
            maxCount = currentCount;
        }
        count++;
    }
    cout<<maxCount;
}
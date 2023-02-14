#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

vector<string> fizzBuzz(int n);

int main()
{
    int n;
    cout << "enter a number lol: ";
    cin >> n;
    vector<string> vectoid = fizzBuzz(n);

    for(int i=0;i<vectoid.size();i++)
    {

    }
}

/*
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
*/
vector<string> fizzBuzz(int n)
{
    vector<string> resultantVector;
    for(int i=1;i<n;i++)
    {
        if(i%3==0&&i%5==0)
        {
            // This will place FizzBuzz into the resultant vector
            resultantVector.push_back("FizzBuzz");

        } 
        else if(i%3==0)
        {
            // This will place Fizz into the resultant vector
            resultantVector.push_back("Fizz");
        }
        else if (i%5==0)
        {
            // This will place Buzz into the resultant vector
            resultantVector.push_back("Buzz");
        } 
        else 
        {
            // This will place i as a string into the resultant vector
            string s =  to_string(i);
            resultantVector.push_back(s);

        }
    }
    return resultantVector;
}
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
int numberOfSteps(int n);

int main()
{
    int n;
    cout << "Put a number: ";
    cin >> n;
    int x = numberOfSteps(n);
    cout << "\nIt Took "<<x<<" steps to reduce "<<n;

}

int numberOfSteps(int n)
{   
    int counter = 0;
    while(n!=0)
    {
        if(n%2==0)
        {
            // Because the number is even, we just divide by 2 and loop
            n=n/2;
            counter++;
        } else 
        {
            // Because the number is odd, we subtract one and loop
            n=n-1;
           // n=n/2;
           counter++;
        }
    }
    return counter;
}
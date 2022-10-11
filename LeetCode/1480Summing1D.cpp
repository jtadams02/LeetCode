#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char* argv[])
{
    vector<int> vectoid;
    for(int i=1;i<argc;i++)
    {
        int thing = atoi(argv[i]);
        vectoid.push_back(thing);
    }
    cout << vectoid.size(); 
    int sum = 0;
    for(vector<int>::iterator i = vectoid.begin();i!=vectoid.end();i++)
    {
        sum += *i;
    }
    cout << sum;
}

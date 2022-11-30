#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

struct ListNode 
{
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* middleNode(ListNode* head);

int main()
{
}

 ListNode* middleNode(ListNode* head) 
{
    // Lets loop through the nodes first
    int counter=0;
    ListNode *temp = head; // 1,2,3,4,5,6
    while(temp!=nullptr)
    {
        counter++;
        temp=temp->next;
    }

    if(counter%2==0)
    {
        // We'll return the middle + 1
        // Ex: 1,2,3,4,5,6 would return 4
        ListNode* test = head->next;
        int match = counter/2;
        for(int i=1;i<counter;i++)
        {
            if(i==match){return test;}
            test=test->next;
        }

    } 
    else
    {
        // This means there will be only 1 answer
        ListNode* test = head->next;
        int match = counter/2;
        for(int i=1;i<counter;i++)
        {
            if(i==match){return test;}
            test=test->next;
            
        }

    }
        return head;
}
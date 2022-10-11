#include <iostream>
#include <math.h>
using namespace std;
struct TreeNode {
     int val;
     TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int main(){
    cout << "Enter Values of Root, Left and Right";
    int r,x,y;
    cin >> r;
    cin >> x;
    cin >> y;

    TreeNode* root = new TreeNode();
    root->val = r;
    TreeNode *left = new TreeNode(x);
    TreeNode *right = new TreeNode(y);

    root->left = left;
    root->right = right;
    int max = root->val;
    int one = root->left->val;
    int two = root->right->val;
    if(max==one+two)
    {
        cout << "true";
    }

    return 0;
}
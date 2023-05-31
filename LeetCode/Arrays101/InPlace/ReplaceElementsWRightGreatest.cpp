class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        // Replace each element with the greatest element to it's right

        // To do this, we're going to need to work backwards. Why? Because this is the most efficient way
        // Instead of having to loop through the rest of the array, we can just look at the value to the right of the current index
        // This value will always be the greatest of all ements on the right



        // Do we need to handle the edge case where we start at the end of the array?


        // Nested loop solution O(N^2)
        for(int i=0;i<arr.size()-1;i++){
            int max = arr[i+1];
            for(int j=i+1;i<arr.size();i++){
                if(max<arr[j]){max = arr[j];}
            }

            arr[i] = max;
        }

        arr[arr.size()] = -1;
    }
};
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        // Time Complexity: O(nlogn)
        // Space Complexity: O(n)
        unordered_map<int, int> map;
        for(int num: arr) map[num]++;
        vector<int> freqs;
        for(auto i: map) freqs.push_back(i.second);
        sort(freqs.begin(), freqs.end());
        int total = freqs.size();
        for(int freq: freqs) {
            if(freq <= k) {
                total -= 1;
                k -= freq;
            } else break;
        }
        return total;
    }
};

// Approach:
// Use a hashmap to calculate the frequencies of elements in arr.
// Store the frequencies in an array and sort them in ascending order.
// Iterate over the sorted array to remove at most k elements, keeping track of the elements completely removed.
// Return the remaining number of unique elements.

// Time Complexity: O(nlogn)
// Space Complexity: O(n)

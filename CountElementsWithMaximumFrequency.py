class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        maxfreq = 0
        d = {}
        result = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
            maxfreq = max(maxfreq, d[num])
        for i in d:
            if d[i] == maxfreq: result += maxfreq
        return result

# Approach:
# Begin by initializing a dictionary d to track the frequency of each element in the given list nums. Each element's frequency is stored as the value, with the element itself as the key.
# Initialize a variable maxfreq to 0. This variable will be used to store the maximum frequency encountered among all elements in nums.
# Iterate through each number in nums. For each number encountered, update its frequency in the dictionary d using the get() method. Increment the frequency by 1 if the element is already present, or initialize it to 1 if it's not.
# While updating the frequency, also update maxfreq to keep track of the maximum frequency encountered so far.
# Initialize a variable result to 0, which will accumulate the sum of frequencies for elements with the maximum frequency.
# Iterate through the keys in the dictionary d. For each element, if its frequency equals maxfreq, increment result by maxfreq.
# Finally, return the value of result, representing the sum of frequencies of elements with the maximum frequency in the list nums.
    
# Time Complexity: O(n)
# Space Complexity: O(n)

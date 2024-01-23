class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Time Complexity: O(2^n)
        # Space Complexity: O(n)
        n = len(arr)
        return self.util(arr, 0, n, [0]*26)

    def util(self, arr, i, n, freq):
        if i == n: return sum(freq)
        result = self.util(arr, i+1, n, freq)
        new = [x for x in freq]
        for ch in arr[i]:
            if new[ord(ch)-97] > 0: break
            new[ord(ch)-97] += 1
        else:
            result = max(result, self.util(arr, i+1, n, new))
        return result

# Approach:
# Check for all sebsequences with unique characters, return the length of longest such subsequence.

# Time Complexity: O(2^n)
# Space Complexity: O(n)

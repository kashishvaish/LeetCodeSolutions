class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        res = []
        for i in range(1, 10):
            n = i
            while n <= high:
                if low <= n <= high:
                    res.append(n)
                d = n % 10
                if d == 9: break
                n = 10*n + d + 1       
        return sorted(res)

# Approach:
# Generate sequential digits within the given range by starting with each digit from 1 to 9.
# Iteratively construct sequential numbers from that starting digit.
# Each number is checked if it falls within the given range [low, high].
# If it does, the number is appended to the result list.
# Finally, the resulting list of sequential digits is sorted before being returned.
# The time complexity is considered O(1) because the loops' size is constant, being bounded by the fixed range of sequential digits [1, 9].

# Time Complexity: O(1)
# Space Complexity: O(1)

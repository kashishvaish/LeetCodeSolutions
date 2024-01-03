class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Time Complexity: O(mn)
        # Space Complexity: O(1)
        m = len(bank)
        if m == 0: return 0
        total = 0
        current = 0
        for i in range(m):
            devices = bank[i].count("1")
            if devices:
                if current:
                    total += devices * current
                current = devices
        return total

# Intuition:
# We can count the number of laser beams by keeping track of the number of security devices in the previous row, ignoring the rows without safety devices.

# Time Complexity: O(mn)
# Space Complexity: O(1)

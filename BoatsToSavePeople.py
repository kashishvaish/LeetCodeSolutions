class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        people.sort(reverse=True)
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if l == r:
                l += 1
            else:
                if people[l] + people[r] <= limit:
                    l += 1
                    r -= 1
                else:
                    l += 1
            count += 1
        return count

# Approach - Two-Pointer:
# Sort the people array in non-increasing order of their weights. This helps in pairing heavier people first, potentially minimizing the number of boats required.
# Initialize two pointers, l and r, pointing to the start and end of the sorted people array, respectively.
# Initialize a variable count to track the number of boats required.
# Iterate while the left pointer l is less than or equal to the right pointer r.
# If l and r point to the same person (i.e., l == r), it means there's only one person left, and they need a separate boat. Increment l to move to the next person.
# If the sum of weights of people at l and r is less than or equal to the limit:
# Increment l to move to the next person from the heavier end.
# Decrement r to move to the next person from the lighter end.
# If the sum of weights exceeds the limit, only increment l to move to the next person from the heavier end.
# Increment the count after each boat is filled or a single person boards the boat.
# After iterating through all people, return the count, which represents the minimum number of boats required to carry everyone.

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(n) due to sorting

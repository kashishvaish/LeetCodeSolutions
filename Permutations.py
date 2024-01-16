class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(NxN!)
        # Space Complexity: O(NxN!)
        n = len(nums)
        if n == 0: return []
        permutations = []
        self.getpermutations(n, nums, 0, set(), [], permutations)
        return permutations

    def getpermutations(self, n, nums, count, set, curr, permutations):
        if count == n:
            permutations.append(curr)
            return
        for i in nums:
            if i not in set:
                self.getpermutations(n, nums, count+1, set.union({i}), curr+[i], permutations)

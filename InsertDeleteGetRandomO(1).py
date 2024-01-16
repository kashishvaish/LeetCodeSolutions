import random

class RandomizedSet:

    def __init__(self):
        # Time Complexity: O(1)
        self.values = [] 
        self.map = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        # Time Complexity: O(1)
        if val in self.map: return False
        self.map[val] = self.count
        self.values.append(val)
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        # Time Complexity: O(1)
        if val not in self.map: return False
        idx = self.map[val]
        self.values[idx] = self.values[-1]
        self.map[self.values[-1]] = idx
        self.values.pop()
        del self.map[val]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        # Time Complexity: O(1)
        ind = random.randint(0, self.count-1)
        return self.values[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Approach:
# Use a list to store the values. This is needed for accessing the elements randomly using index in O(1) time.
# Use a dictionary/hashmap to store the values and their corresponding indexes in the list. This is done to enable searching and removing elements in O(1) time.

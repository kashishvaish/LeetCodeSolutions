class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        counter = [0] * 26
        max_val = 0
        max_count = 0

        for task in tasks:
            counter[ord(task) - ord('A')] += 1
            if max_val == counter[ord(task) - ord('A')]:
                max_count += 1
            elif max_val < counter[ord(task) - ord('A')]:
                max_val = counter[ord(task) - ord('A')]
                max_count = 1
        
        part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles
    
# Approach:
# Initialize a counter array of size 26 to store the frequency of each task and variables maximum and maxCount to track the maximum frequency and the number of tasks with that frequency.
# Traverse through the tasks and update the counter array. If the frequency of a task is equal to the current maximum frequency, increment maxCount. If the frequency is greater than the current maximum frequency, update maximum and set maxCount to 1.
# Calculate the number of emptySlots by multiplying partCount (maximum frequency - 1) and partLength (cooldown period - (number of tasks with maximum frequency - 1)).
# Calculate the number of availableTasks by subtracting the product of maximum and maxCount from the total number of tasks.
# Calculate the number of idle periods needed by taking the maximum of 0 and the difference between the number of emptySlots and the number of availableTasks.
# Return the total time required by adding the number of tasks to the number of idle periods.
    
# Time Complexity: O(n)
# Space Complexity: O(1)

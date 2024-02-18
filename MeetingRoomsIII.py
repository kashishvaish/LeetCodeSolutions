class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Time Complexity: O(mlogm + mn)
        # Space Complexity: O(m + n)
        whenwillbefree = [-1]*n
        count = [0]*n
        meetings.sort()
        for meeting in meetings:
            minfree = -1
            room = -1
            for i, t in enumerate(whenwillbefree):
                if t <= meeting[0]:
                    whenwillbefree[i] = meeting[1]
                    count[i] += 1
                    break
                if minfree == -1 or whenwillbefree[i] < minfree:
                    minfree = whenwillbefree[i]
                    room = i
            else:
                whenwillbefree[room] += meeting[1]-meeting[0]
                count[room] += 1
        maxcount = -1
        ind = -1
        for i in range(n):
            if count[i] > maxcount:
                maxcount = count[i]
                ind = i
        return ind
                
# Approach:
# Initialize two arrays, whenwillbefree and count, both of size n, to keep track of the availability time for each room and the count of meetings held in each room, respectively.
# Iterate through each meeting in the sorted order based on their start times.
# For each meeting, find the earliest available room by iterating through the whenwillbefree array. If a room is available (its availability time is less than or equal to the current meeting's start time), allocate the meeting to that room, update the meeting count for that room, and set the room's availability time to the meeting's end time. Break out of the loop.
# If no available room is found, find the room with the earliest availability time. Update the availability time for that room to accommodate the delayed meeting, and increment the meeting count for that room.
# After processing all meetings, return the index of the room with the maximum meeting count.
     
# Example:
# n = 2        
# whenwillbefree = [-1, -1]
# meetings = [[0,10],[1,5],[2,7],[3,4]]
# count = [0, 0]

# for [0, 10]
# whenwillbefree = [10, -1]
# count = [1, 0]

# for [1, 5]
# whenwillbefree = [10, 5]
# count = [1, 1]

# for [2, 7] -> duration = 5 --> wait till time = 5 for room at 1st index to be empty
# whenwillbefree = [10, 10]
# count = [1, 2]

# for [3, 4] -> duration = 1 --> wait till time = 10 for room at 0th index to be empty
# whenwillbefree = [11, 10]
# count = [2, 2]

# return 0 as both room 0 and room 1 have counts equal to 2

# Time Complexity: O(mlogm + mn)
# Space Complexity: O(m + n)

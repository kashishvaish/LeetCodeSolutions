# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        graph = {}
        self.creategraph(root, -1, graph)
        queue = [start]
        minute = 0
        visited = {start}
        while queue:
            n = len(queue)
            while n > 0:
                node = queue.pop(0)
                for adj in graph[node]:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
                n -= 1
            minute += 1
        return minute - 1

    def creategraph(self, node, parent, graph):
        if not node: return
        graph[node.val] = set()
        if parent != -1:
            graph[node.val].add(parent) 
        if node.left:
            graph[node.val].add(node.left.val)
            self.creategraph(node.left, node.val, graph)
        if node.right:
            graph[node.val].add(node.right.val)
            self.creategraph(node.right, node.val, graph)

# Approach
# First, convert the tree to an undirected graph, and then perform breadth first search starting from the start node to get the maximum distance between start and the rest of the nodes.

# Time Complexity: O(n)
# Space Complexity: O(n)

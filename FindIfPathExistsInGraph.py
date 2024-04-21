class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Time Complexity: O(n + e)
        # Space Complexity: O(n + e)
        visited = [False]*n
        graph = {i:[] for i in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)
            if u == destination: return True
            for v in graph[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        return False
    
# Approach - Breadth First Search
# Initialize a boolean array visited of size n to keep track of visited nodes, initially set to False.
# Initialize a dictionary graph to represent the graph, where keys are nodes and values are lists of adjacent nodes.
# Populate the graph dictionary based on the given edges list.
# Start BFS from the source node.
# Enqueue the source node into the queue and mark it as visited.
# While the queue is not empty:
# Dequeue a node u from the queue.
# If u is the destination node, return True since a valid path exists.
# Otherwise, iterate through each adjacent node v of u:
# If v has not been visited yet, enqueue v into the queue and mark it as visited.
# If the destination node is not reached during BFS, return False, indicating that there is no valid path from the source to the destination.
    
# Time Complexity: O(n + e)
# Space Complexity: O(n + e)

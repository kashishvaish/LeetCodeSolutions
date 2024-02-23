class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time Complexity: O(V + E)
        # Space complexity:O(V + E)
        graph = {i:[] for i in range(n)}
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        dist = [float('inf')]*n
        dist[src] = 0
        queue = [(src, -1, 0)]
        while queue:
            curr, stop, prize = queue.pop(0)
            if stop < k:
                for d, p in graph[curr]:
                    if prize + p >= dist[d]: continue
                    dist[d] = prize + p
                    queue.append((d, stop+1, prize+p))
        return dist[dst] if dist[dst] != float('inf') else -1
    
# Approach:
# Create a dictionary where each city is a key, and the value is a list of tuples representing neighboring cities and the cost of the flights.
# Initialize an array to keep track of the minimum cost to reach each city from the source city.
# Set the cost of reaching the source city itself to 0 and the cost of reaching all other cities to infinity initially.
# Start BFS traversal from the source city.
# Traverse the graph one level at a time, considering all possible flights from the current city.
# At each step, update the minimum cost to reach each neighboring city if a cheaper route is found through the current city.
# Keep track of the number of stops made during BFS traversal.
# Stop BFS traversal when the maximum number of stops k is reached.
# After BFS traversal, check if the destination city is reachable within the specified number of stops.
# If reachable, return the minimum cost to reach the destination city.
# If not reachable within the specified number of stops, return -1.

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space complexity:O(V + E), where V is the number of vertices and E is the number of edges in the graph.

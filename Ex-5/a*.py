import heapq

def a_star(graph, start, goal, h):
    # Priority queue to store (cost, current_node, path)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        # If the goal is reached, return the path and cost
        if current == goal:
            return path, cost

        # Skip already visited nodes
        if current in visited:
            continue
        visited.add(current)

        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                total_cost = cost + weight
                priority = total_cost + h[neighbor]
                heapq.heappush(pq, (priority, neighbor, path + [neighbor]))

    return None, float('inf')  # Return None if no path is found

# Example graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('E', 1)],
    'D': [('F', 2)],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values (h) for each node
heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 2, 'E': 2, 'F': 0
}

# Run A* algorithm
start_node = 'A'
goal_node = 'F'
path, cost = a_star(graph, start_node, goal_node, heuristic)

print("Shortest Path:", path)
print("Cost:", cost)

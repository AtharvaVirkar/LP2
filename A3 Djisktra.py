def dijkstra(graph, src):
    dist = {vertex: float('inf') for vertex in graph}  # Dictionary to store the shortest distance from source to each vertex
    visited = {vertex: False for vertex in graph}  # Dictionary to keep track of visited vertices
    prev = {vertex: None for vertex in graph}  # Dictionary to store the predecessor of each vertex in the shortest path
    dist[src] = 0  # Distance from source to itself is 0
    while True:
        u = min(dist, key=dist.get)  # Find the vertex with the minimum distance
        if visited[u]:  # If the vertex has been visited, break the loop
            break
        visited[u] = True  # Mark the vertex as visited
        for v in graph[u]:  # Update the distance of the adjacent vertices
            if not visited[v] and dist[u] + graph[u][v] < dist[v]:  # If the new distance is shorter, update
                dist[v] = dist[u] + graph[u][v]  # Update the distance to vertex v
                prev[v] = u  # Set the predecessor of vertex v
    return dist, prev  # Return the shortest distances and predecessors

# Define the graph using an adjacency list representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Call the Dijkstra's algorithm function with the graph and source vertex
dist, prev = dijkstra(graph, 'A')

# Print the shortest distances and predecessors from vertex A
print('Shortest distances from vertex A:')
for vertex, distance in dist.items():
    print(f'Vertex {vertex}: Distance = {distance}, Predecessor = {prev[vertex]}')

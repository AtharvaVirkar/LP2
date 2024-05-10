def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = [start]  # Initialize a queue with the start node
    while queue:  # Continue traversal while the queue is not empty
        node = queue.pop(0)  # Dequeue a node from the front of the queue
        if node not in visited:  # Check if the node has not been visited
            visited.append(node)  # Mark the node as visited
            queue.extend(graph[node])  # Enqueue adjacent nodes to the queue
    return visited  # Return the list of visited nodes

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    visited.add(start)  # Mark the current node as visited
    print(start, end=' ')  # Print the current node
    for next_node in graph[start]:  # Explore adjacent nodes
        if next_node not in visited:  # Check if the node has not been visited
            dfs(graph, next_node, visited)  # Recursive call with the adjacent node

# Define the graph using an adjacency list representation
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# Breadth-First Search (BFS) traversal
print("Breadth-First Search:")
bfs_result = bfs(graph, '5')  # Call BFS function with the graph and start node
print(*bfs_result)  # Print the result of BFS traversal

# Depth-First Search (DFS) traversal
print("\nDepth-First Search:")
dfs(graph, '5')  # Call DFS function with the graph and start node

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Set of nodes to be evaluated
    closed_set = set()  # Set of nodes already evaluated
    g = {start_node: 0}  # Cost from start node to each node
    parent = {start_node: start_node}  # Parent nodes for constructing the path
    
    while len(open_set) > 0:  # Continue until all nodes have been evaluated
        n = None  # Initialize the current node to None
        
        # Find the node with the lowest cost from the start node
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        # Check if the current node is the goal node or it has no neighbors
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            # Explore neighbors of the current node
            for m, weight in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    # Add neighbor to the open set
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                
                else:
                    # Update cost if a shorter path is found
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        
                        if m in closed_set:
                            # Move neighbor from closed set to open set
                            closed_set.remove(m)
                            open_set.add(m)
                            
        # Check if a path exists or if the goal node has been reached
        if n is None:
            print("Path does not exist!")
            return None
        
        if n == stop_node:
            # Reconstruct the path from start node to goal node
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path
        
        open_set.remove(n)  # Remove the current node from open set
        closed_set.add(n)  # Add the current node to closed set
    
    print("Path does not exist!")  # If loop ends without finding the goal node
    return None

def get_neighbours(v):
    # Get neighbors of a node from the graph
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    # Heuristic function to estimate cost from node n to goal node
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist[n]

# Define the graph using an adjacency list representation
Graph_nodes = {'A': [('B', 2), ('E', 3)], 'B': [('A', 2), ('C', 1), ('G', 9)], 'C': [('B', 1)], 'D': [('E', 6), ('G', 1)], 'E': [('A', 3), ('D', 6)], 'G': [('B', 9), ('D', 1)]}

start_node = input("Enter start node: ")  # Input start node from user
stop_node = input("Enter stop node: ")  # Input stop node from user
aStarAlgo(start_node, stop_node)  # Call the A* algorithm function

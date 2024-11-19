# Depth First Search Algorithm

graph = {
    '0': {'1', '2'},     # Node 0 is connected to nodes 1 and 2
    '1': {'0', '3', '4'}, # Node 1 is connected to nodes 0, 3, and 4
    '2': {'0'},          # Node 2 is connected to node 0
    '3': {'1'},          # Node 3 is connected to node 1
    '4': {'2', '3'}  # Node 4 is connected to nodes 2 and 3
}

def dfs(graph, start, visited=None):
    if visited is None:        # Initialize visited set on first call
        visited = set()
    visited.add(start)        # Mark current node as visited
    print(start)             # Print current node

    # Explore unvisited neighbors
    for next in graph[start] - visited:  # Subtract visited nodes from neighbors
        dfs(graph, next, visited)        # Recursive call for each unvisited neighbor
    return visited

dfs(graph, '0')

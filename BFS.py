# Breadth First Search Algorithm

graph = {
    '5': ['3','7'],   # Node 5 is connected to nodes 3 and 7
    '3': ['2','4'],   # Node 3 is connected to nodes 2 and 4
    '7': ['8'],       # Node 7 is connected to node 8
    '2': [],          # Node 2 has no connections
    '4': ['8'],       # Node 4 is connected to node 8
    '8': []           # Node 8 has no connections
}

visited = []      # To keep track of visited nodes
queue = []  # To manage nodes to be explored


def BFS(visited, graph, node):
    visited.append(node)  # Mark start node as visited
    queue.append(node)  # Add start node to queue

    while queue:  # While there are nodes to explore
        m = queue.pop(0)  # Get the first node from queue
        print(m, end=" ")  # Print the current node

        # Explore all neighbors of current node
        for n in graph[m]:
            if n not in visited:  # If neighbor not visited
                visited.append(n)  # Mark as visited
                queue.append(n)  # Add to queue

print("BFS is: ")
BFS(visited,graph,'5')

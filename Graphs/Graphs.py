# This is the graph [images/sample_graph2.png]
from collections import deque

graph = {
    "1": ["2", "3"],
    "2": ["5"],
    "3": ["2", "4", "6"],
    "4": ["6"],
    "5": ["8"],
    "6": ["3", "7"],
    "7": ["2"],
    "8": ["7"],
    "9": ["8", "7"],
}

def bfs(start):
    queue = deque([start])
    seen = set([start])

    while queue:
        print(queue[0], seen)
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

print("BFS")
bfs("1")

# Use BFS to find shortest path
# Bipartite graph means you can color nodes one of two colors such that no edge connects nodes of the same color
# Graph is bipartite if and only if it has no odd length cycles

def dfs_iter(start):
    stack = [start]
    seen = set([start])

    while stack:
        print(stack[-1], seen)
        current = stack.pop()

        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

print("Iterative DFS")
dfs_iter("1")

def dfs_recur(start, seen):
    print(start, seen)

    for nei in graph[start]:
        if nei not in seen:
            seen.add(nei)
            dfs_recur(nei, seen)

print("Recursive DFS")
seen = set(["1"])
dfs_recur("1", seen)

# DFS edge types [images/graph_edges.png]
# You can check for cycles by looking for back edges
# DFS sweep to process all nodes in a graph [images/dfs_sweep.png]
# Topoligical sort is sorting by reverse order of finish times with DFS sweep [images/topolgical_sort.png]

# Explore strongly connected components, dijkstra's, MSTs (prims, kruskal), Min/max flow
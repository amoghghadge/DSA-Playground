from collections import defaultdict
from typing import List

class Solution:
    # n is number of nodes (labeled from 0 to n - 1 inclusive), edges is list of directed edges in form (src, dest)
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)      # for generic topological sort, build the graph in reverse order to use this algorithm
        # for the way edges are given in Course Schedule II it would be graph[a].append(b)
        
        # True means node has already been processed (prevents double processing), False means node is in current path (helps detect cycles)
        visiting = {}
        path = []
        
        def dfs(curr):
            if curr in visiting:
                return visiting[curr]

            visiting[curr] = False
            
            for nei in graph[curr]:
                if not dfs(nei):
                    return False
            
            visiting[curr] = True
            path.append(curr)
            return True
        
        # DFS sweep to find topological ordering, where nodes with no edges going anywhere come first
        # Think of directed edges as prereqs: before being able to process the source node you must process the destination nodes
        for i in range(n):
            if not dfs(i):
                return []       # edges form a cycle, ordering is not possible, return empty list
        
        return path

ans = Solution()
print(ans.topologicalSort(n = 5, edges = [[0, 2], [0, 1], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
print(ans.topologicalSort(n = 5, edges = [[0, 1], [0, 2], [3, 1], [2, 3], [1, 4], [3, 4]]))
print(ans.topologicalSort(n = 4, edges = [[1,0],[2,0],[3,1],[3,2]]))
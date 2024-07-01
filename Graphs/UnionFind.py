class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.sets = n

    def find(self, n: int):
        if n != self.parent[n]:                                 # go until finding highest parent, where index is equal to its value
            self.parent[n] = self.find(self.parent[n])          # path compression
        
        return self.parent[n]

    def union(self, n1: int, n2: int):              # union by rank
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:                                # already in same set
            return 0
        
        if self.rank[p1] > self.rank[p2]:           # p1 has higher rank, union p2 under p1
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        else:                                       # p2 has higher rank, union p1 under p2
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]
        
        self.sets -= 1                              # two sets were merged together, count of sets decreases by 1
        return 1

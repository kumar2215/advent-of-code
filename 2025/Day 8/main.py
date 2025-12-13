import heapq
from collections import defaultdict

with open("input.txt") as f:
    points = [tuple(map(int, line.split(","))) for line in f.read().split("\n")]
    indexes = {p: i for i, p in enumerate(points)}

def euclidean_distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.weight = -euclidean_distance(u, v)
        
    def __eq__(self, other):
        return (self.u == other.u and self.v == other.v) or (self.u == other.v and self.v == other.u)

    def __lt__(self, other):
        return self.weight < other.weight
    
    def __repr__(self):
        return f"Edge({self.u}, {self.v}, weight={abs(self.weight)})"
    
    def __hash__(self):
        return hash((self.u, self.v)) ^ hash((self.v, self.u))

L = 1000
h, h2 = [], []
heapq.heapify(h)
heapq.heapify(h2)
n = len(points)
for i in range(n):
    for j in range(i + 1, n):
        edge = Edge(points[i], points[j])
        if len(h) < L: heapq.heappush(h, edge)
        else: heapq.heappushpop(h, edge)
        edge2 = Edge(points[i], points[j])
        edge2.weight = -edge2.weight
        heapq.heappush(h2, edge2)

class UnionFind:
    def __init__(self, lst, pred=None):
        n = len(lst)
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n
        self.groups = defaultdict(list)
        for i in range(n): self.groups[i].append(lst[i])
        if pred:
            for i in range(n):
                for j in range(i + 1, n):
                    if pred(lst[i], lst[j]):
                        self.union(i, j)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.n -= 1
            self.groups[px].extend(self.groups[py])
            del self.groups[py]

S = set(h)
groups = UnionFind(points, lambda p1, p2: Edge(p1, p2) in S).groups
groups = {g: len(groups[g]) for g in groups}

TOP_K = 3
biggest_groups = sorted(groups.items(), key=lambda item: item[1], reverse=True)[:TOP_K]
product = 1
for _, size in biggest_groups:
    product *= size

UF = UnionFind(points)
edge = None
while len(UF.groups) > 1:
    edge = heapq.heappop(h2)
    UF.union(indexes[edge.u], indexes[edge.v])

print(f"Part 1: {product}")
print(f"Part 2: {edge.u[0] * edge.v[0]}")
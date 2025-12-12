import heapq

with open("input.txt") as f:
    lines = [tuple(map(int, line)) for line in f.read().splitlines()]
    
total, total2 = 0, 0
L1, L2 = 2, 12

def build(nums, L):
    N = len(nums)
    W = N - L + 1
    h = []
    heapq.heapify(h)
    l = []
    
    for w in range(L):
        tmp = [(x, i+w) for i, x in enumerate(nums[w:W + w]) if all(i+w > j for j in l)]
        m = max(tmp, key=lambda x: (x[0], -x[1]))
        idx = m[1]
        l.append(idx)
        if len(h) < L:
            heapq.heappush(h, (-m[0], -idx))
        else:
            heapq.heappushpop(h, (-m[0], -idx))
    
    h.sort(key=lambda x: -x[1])
    s = "".join([str(-m[0]) for m in h])
    return int(s)

for line in lines:
    total += build(line, L1)
    total2 += build(line, L2)

print(f"Part 1: {total}")
print(f"Part 2: {total2}")
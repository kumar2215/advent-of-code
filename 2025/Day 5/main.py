
with open("input.txt") as f:
    lines = f.read().splitlines()
    idx = lines.index("")
    ranges = [tuple(map(int, line.split("-"))) for line in lines[:idx]]
    nums = list(map(int, lines[idx+1:]))
    
total = 0
for num in nums:
    for r in ranges:
        if r[0] <= num <= r[1]:
            total += 1
            break
        
intervals = set()
for r in ranges:
    s, e = r
    for interval in intervals.copy():
        if not (e < interval[0] or s > interval[1]):
            s = min(s, interval[0])
            e = max(e, interval[1])
            intervals.remove(interval)
    intervals.add((s, e))
    
total2 = 0
for interval in intervals:
    total2 += interval[1] - interval[0] + 1

print(F"Part 1: {total}")
print(F"Part 2: {total2}")
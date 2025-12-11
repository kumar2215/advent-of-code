
with open("input.txt") as f:
    ranges = f.read().strip()
    ranges = [tuple(map(int, line.split('-'))) for line in ranges.split(',')]
    
total = 0
total2 = 0
for r1, r2 in ranges:
    for x in range(r1, r2 + 1):
        s = str(x)
        L = len(s)
        l = 2
        
        while L // l >= 1:
            if L % l == 0:
                mid = L // l
                parts = [s[i:i+mid] for i in range(0, L, mid)]
                if all(part == parts[0] for part in parts):
                    if l == 2: total += x
                    total2 += x
                    break
            l += 1
            
print(f"Part 1: {total}")
print(f"Part 2: {total2}")
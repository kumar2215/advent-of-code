from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()
    grid = [list(line) for line in lines]
    S = (0, grid[0].index("S"))

D, W = len(grid), len(grid[0])
beams = defaultdict(int)
beams[S] = 1
seen = set()
total = 0
while beams:
    new_beams = defaultdict(int)
    for r, c in beams:
        if r == D-1:
            total += beams[(r, c)]
            continue
        if grid[r+1][c] == ".":
            new_beams[(r+1, c)] += beams[(r, c)]
        else:
            if 0 <= c-1 < W and grid[r][c-1] == ".":
                new_beams[(r, c-1)] += beams[(r, c)]
            if 0 <= c+1 < W and grid[r][c+1] == ".":
                new_beams[(r, c+1)] += beams[(r, c)]
            seen.add((r, c))
    beams = new_beams
    
print(f"Part 1: {len(seen)}")
print(f"Part 2: {total}")
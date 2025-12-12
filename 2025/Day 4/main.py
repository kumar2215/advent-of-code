
with open("input.txt") as f:
    lines = f.read().splitlines()
    grid = [list(line) for line in lines]
    
LIMIT = 4
M, N = len(grid), len(grid[0])
total, total2 = 0, 0

def get_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and 0 <= x + dx < M and 0 <= y + dy < N:
                neighbors.append((x + dx, y + dy))
    return neighbors

itr = 0
while True:
    lst = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if grid[i][j] == '.': continue
            tmp = [(y, x) for x, y in get_neighbors(i, j) if grid[x][y] != '.']
            if len(tmp) < LIMIT: 
                if itr == 0: total += 1
                total2 += 1
                lst.append((i, j))
    if not lst: break
    for i, j in lst:
        grid[i][j] = '.'
    itr += 1
        
print(f"Part 1: {total}")
print(f"Part 2: {total2}")
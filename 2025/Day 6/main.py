with open("input.txt") as f:
    raw_lines = f.read().splitlines()
    lines = [line.strip().split() for line in raw_lines]
    lines = [*zip(*lines)]

def get_total(lines):
    total = 0
    for line in lines:
        if line[-1] == "+":
            total += sum(int(x) for x in line[:-1])
        elif line[-1] == "*":
            prod = 1
            for x in line[:-1]:
                prod *= int(x)
            total += prod
    return total
        
operations = raw_lines[-1]
gaps = []
count = None
for char in operations:
    if char == " ":
        count += 1
    else:
        if count is not None: gaps.append(count)
        count = 0
gaps.append(count + 1)
operations = [char for char in operations if char != " "]

lines2 = []
for line in raw_lines[:-1]:
    new_line = []
    index = 0
    for gap in gaps:
        segment = line[index:index+gap]
        new_line.append(segment)
        index += gap + 1
    lines2.append(new_line)

lines2 = [*zip(*lines2)]
lines2 = [[*zip(*line)] for line in lines2]
lines2 = [["".join(segment).strip() for segment in line]+[operations[i]] for i, line in enumerate(lines2)]

print(f"Part 1: {get_total(lines)}")
print(f"Part 2: {get_total(lines2)}")
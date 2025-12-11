with open("input.txt") as f:
    instructions = f.read().splitlines()

LENGTH = 100
position = 50
count, count2 = 0, 0

for instruction in instructions:
    num = int(instruction[1:])
    flag = False
    
    if instruction[0] == "L":
        if num > position:
            if position != 0:
                count2 += 1
                flag = True
                num -= position
                position = 0
            
            if num >= LENGTH:
                count2 += num // LENGTH
                num = num % LENGTH
            
        position = (position - num) % LENGTH
        
    elif instruction[0] == "R":
        if num > LENGTH - position:
            if position != 0:
                count2 += 1
                flag = True
                num -= (LENGTH - position)
                position = 0
            
            if num >= LENGTH:
                count2 += num // LENGTH
                num = num % LENGTH
        
        position = (position + num) % LENGTH
        
    if position == 0:
        count += 1
        if not flag: count2 += 1
        
print(f"Part 1: {count}")
print(f"Part 2: {count2}")
file1 = open('input.txt', 'r')

id = 1
elves = {}
elves[id] = 0
while True:
    
    line = file1.readline()
    if not line:
        break
    if line == "\n":
        id += 1
        elves[id] = 0
        continue
    elves[id] = int(line) + elves[id]
    

print(sorted(elves.items(), key=lambda x: x[1]))



print(67860+68708+68802)
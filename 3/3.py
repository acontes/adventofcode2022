import math

file1 = open('input.txt', 'r')
# A, X : rock : 1
# B, Y Paper : 2 
# C, Z : Scissor: 3

dict = {}
v = 1

a = ord('a')

for i in range(0,26):
    dict[chr(a+i)] = i+1

a = ord('A')
for i in range(0,26):
    dict[chr(a+i)] = i+27


total = 0

while True:
    line = file1.readline()
    if not line:
        break
    split = math.floor(len(line) / 2)

    

    items1 = line[0:split]
    items2 = line[split:]
    print(line)
    print(items1)
    print(items2)

    r = ''.join(set(items1).intersection(items2))

    print(">>>>" + r)
    if r:
        total += dict[r]

print(total)

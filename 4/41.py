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
    line1 = file1.readline().strip()
    if not line1:
        break

    r = line1.split(',')
    r1 = r[0].split('-')
    r2 = r[1].split('-')

    print(r1,r2)

    s1 = set(range(int(r1[0]), int(r1[1])+1))
    s2 = set(range(int(r2[0]), int(r2[1])+1))

    print(s1,s2)

    if s1.intersection(s2):
        total += 1
        print('^^')

print(total)

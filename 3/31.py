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
    line1 = file1.readline()
    if not line1:
        break
    line2 = file1.readline()
    if not line2:
        break
    line3 = file1.readline()
    if not line3:
        break

    line1 = line1.strip()
    line2 = line2.strip()
    line3 = line3.strip()
    r1 = ''.join(set(line1).intersection(line2).intersection(line3))

    if r1:
        total += dict[r1]

print(total)

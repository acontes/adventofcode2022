import math

file = open('input.txt', 'r')
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
queues = [ [] for q in range(9) ]


position = -1
# 1st part
# NB = 4
#2nd part
NB = 14
while True:
    line1 = file.readline().strip()
    if not line1:
        break

    for i in range(len(line1)):
        s= set()
        for j in range(NB):
            s.add(line1[i+j])
        if len(s) == NB:
            position = i
            print(position+NB)
            break




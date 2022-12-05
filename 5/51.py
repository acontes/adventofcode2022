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


for i in range(8):
    line = file.readline()
    for i in range(9):
        c = line[(i*4) + 1]
        if c != ' ':
            queues[i].append(c)

print(queues)

#skip next 2 lines
file.readline()
file.readline()

NB = 1
FROM = 3
TO = 5
linenb = 11
stop = 5
while True:
    line1 = file.readline().strip()
    print(" >>> " + line1)
    if not line1:
        break

    action = line1.split(' ')

    for i in range(int(action[NB])):
        f = queues[int(action[FROM])-1].pop(0)
        queues[int(action[TO])-1].insert(i,f)


    print(queues)
    stop -= 1
    if (stop == 0):
        pass


for i in range(9):
    print(queues[i][0],end='')

print()

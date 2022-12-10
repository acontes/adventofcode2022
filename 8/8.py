import math

file = open('input.txt', 'r')
# A, X : rock : 1
# B, Y Paper : 2
# C, Z : Scissor: 3

forest = []

while True:

    line1 = file.readline().strip()
    if not line1:
        break

    l = [ int(n) for n in line1 ]
    forest.append(l)

dir = {"x":0,"y":1}


def visible_in_line(line,x):
    target_high = line[x]
    print(">>> x:%s|high:%s;line=%s;" % (x,target_high,line))
    
    for ii in line[0:x]:
        print(">>" + str(ii))
        if ii>=target_high:
            return False
    
    print("<<<")
    return True

total = 0

def visible(forest,x,y):
    
    print("testing %s,%s" % (x,y))
    if visible_in_line(forest[x],y):
        print("visible l")
        return True

    reverse_x = [ f for f in reversed(forest[x])]

    if visible_in_line(reverse_x,len(forest[x]) - 1 - y):
        print("visible rl")
        return True

    # column
    c = [ f[y] for f in forest]
    if visible_in_line(c,x):
        print("visible c")
        return True

    reverse_c = [ f for f in reversed(c)]
    if visible_in_line(reverse_c,len(c) - 1 - x):
        print("visible rc")
        return True
   
    return False

array_len = len(forest[0])
print("length:%s" % array_len)
for i in range(1,array_len-1):
    for j in range(1, array_len-1):
        if visible(forest,i,j):
            total += 1

total = total + len(forest)*2 + (len(forest)-2)*2
print(total)

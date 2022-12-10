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
    high = target_high = line[x]
    print(">>> x:%s|high:%s;line=%s;" % (x,target_high,line))
  
    distance = 0
    print(line[0:x])
    for ii in reversed(line[0:x]):
        distance +=1
        if ii>=high:
            break

    #print("<<< [%s] -> %s" % (x,distance))
    return distance

total = 0

def visible(forest,x,y):
    aa = bb = cc = dd = 1
    print("testing %s,%s" % (x,y))
    aa = visible_in_line(forest[x],y)

    reverse_x = [ f for f in reversed(forest[x][y:])]
    bb = visible_in_line(reverse_x,len(reverse_x)-1)

    # column
    c = [ f[y] for f in forest]
    cc = visible_in_line(c,x)
     
    reverse_c = [ f for f in reversed(c[x:])]
    dd = visible_in_line(reverse_c,len(reverse_c)-1)
    print("left=%s,right=%s,up=%s,down=%s" % (aa,bb,cc,dd))
    return aa * bb * cc * dd

array_len = len(forest[0])
print("length:%s" % array_len)
score = 0
for i in range(1,array_len-1):
    for j in range(1, array_len-1):
        c = visible(forest,i,j)
        if c > score:
            score = c


print(score)

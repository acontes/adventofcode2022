import math

file = open('input.txt', 'r')
# A, X : rock : 1
# B, Y Paper : 2 
# C, Z : Scissor: 3


class Node:
    def __init__(self,name,parent,size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

    # print function
    def PrintTree(self):
        print(self.data)

    def add(self, node):
        self.size += node.size
        self.children.append(node)

    def __str__(self):
        return "{{%s:%s}}" % (self.name, self.size)

    def __repr__(self):
        return "Node(%s,%s)" % (self.name, self.size)

    def compute(self):
        if not self.children:
            return
        self.size = 0
        for n in self.children:
            if n.children:
                n.compute()
            self.size += n.size


def display(node, padding):
    if node.children: 
        print("%s - %s :d|%s " % (padding,node.name,node.size))
    else:
        print("%s - %s :f|%s " % (padding,node.name,node.size))
    for i in node.children:
        display(i, padding + "  ")

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
root = None
tree = None
while True:

    line1 = file.readline().strip()
    if not line1:
        break

    action = line1.split(' ')

    match action[0]:
        case "$":
            match action[1]:
                case "cd":
                    if action[2] == "..":
                        if tree and tree.parent:
                            tree = tree.parent
                            tree.compute()
                    else:
                        t = Node(action[2],tree,0)
                        if tree:
                            tree.add(t)
                            tree = t
                        else:
                           root = tree = t
        case "dir":
            pass
        case _:
            tree.add(Node(action[1],tree,int(action[0])))
        

def inspect(node,v):

    if not node:
        return []
    
    if not node.children:
        return []

    c = []
    for n in node.children:
        r = inspect(n,v)
        if r:
            c += r

    if node.size >= v:
        c.append(node)
    return c


root.compute()

display(root, "")

capacity = 70000000
needed = 30000000
allocated = root.size
remaining = capacity - root.size

tofree = (remaining - needed)
if tofree < 0:
    tofree *= -1

print(tofree)
a = inspect(root,tofree)
print(sorted(a,key=lambda node : node.size))
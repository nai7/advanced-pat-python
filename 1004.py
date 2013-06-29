def toInt(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

nTotal,nNonLeaf = toInt(raw_input().split())

parent = [0]*(nTotal+1)
for i in range(nNonLeaf):
    lst = toInt(raw_input().split())
    for i in range(lst[1]):
        parent[lst[i+2]] = lst[0]

nLeaf = [0]*nTotal
nMaxLevel = 0
def CountLeaves(node,level):
    global nTotal,parent,nLeaf,nMaxLevel

    isLeaf = True
    for i in range(1,nTotal+1):
        if node==parent[i]:
            CountLeaves(i,level+1)
            isLeaf = False
    if isLeaf:
        if level+1 > nMaxLevel:
            nMaxLevel = level + 1
        nLeaf[level] += 1

CountLeaves(1,0)

for i in range(nMaxLevel):
    print nLeaf[i],
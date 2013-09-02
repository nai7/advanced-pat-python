N, head = raw_input().split()
nodes = {}
for i in xrange(int(N)):
    addr, key, next = raw_input().split()
    nodes[addr] = (key, next)
lst = []
addr = head
while addr != '-1':
    lst.append((addr, nodes[addr][0]))
    addr = nodes[addr][1]
lst.sort(lambda a1, a2: cmp(a1[1], a2[1]))
if not lst:
    print 0 ,-1
    exit(0)
l = len(lst)
print l, lst[0][0]
print lst[0][0],
for i in xrange(l-1):
    print lst[i][1], lst[i+1][0]
    print lst[i+1][0],
print lst[l-1][1], -1
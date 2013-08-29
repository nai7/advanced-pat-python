node1, node2, N = raw_input().split()
nodes = {}
for n in xrange(int(N)):
    start_node, data, end_node = raw_input().split()
    nodes[start_node] = end_node

path = []
while not node1=='-1':
    path.append(node1)
    node1 = nodes[node1]
while not (node2 in path or node2=='-1'):
    node2 = nodes[node2]
print node2
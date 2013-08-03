N = input()
gmap = [[] for n in xrange(N+1)]
pnt  = [0] * (N+1)
def root(n):
    if not pnt[n]:
        return n
    else:
        return root(pnt[n])
for i in xrange(N-1):
    n1, n2 = map(int, raw_input().split())
    gmap[n1].append(n2)
    gmap[n2].append(n1)
    root1, root2 = map(root, (n1, n2))
    if not root1==root2:
        pnt[root1] = root2

count = 0
for p in pnt[1:]:
    if not p: count += 1
if count != 1:
    print 'Error:', count, 'components'
    exit(0)

from Queue import Queue
deepest_roots = set()
def bfs(n):
    q = Queue()
    q.put(n)
    deepth = [0] * (N+1)
    max_deepth = 0
    deepth[n] = 1
    while not q.empty():
        now = q.get()
        if deepth[now] > max_deepth:
            max_deepth = deepth[now]
        for next in gmap[now]:
            if not deepth[next]:
                deepth[next] = deepth[now] + 1
                q.put(next)
    for n, d in enumerate(deepth):
        if d==max_deepth:
            deepest_roots.add(n)
bfs(1)
for s in deepest_roots:
    bfs(s)
    break
for s in sorted(deepest_roots):
    print s
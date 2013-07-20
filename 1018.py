import sys
MAX_INT = sys.maxint
def get_line():
    return map(int, raw_input().split())
CMAX, N, sp, R = get_line()
bikes = [0] + map(lambda a: a - CMAX/2, get_line())
costs = [[] for i in xrange(N+1)]
for i in xrange(R):
    s1, s2, cost = get_line()
    if s1 and s2 - sp: costs[s1].append((s2,cost))
    if s2 and s1 - sp: costs[s2].append((s1,cost))

dis = [MAX_INT] * (N+1)
visited = [False] * (N+1)
dis[sp] = 0
queue = [sp]
parent = [0] * (N+1)
need = [0] * (N+1)
back = [0] * (N+1)
need[sp], back[sp] = (CMAX/2, 0) if bikes[sp]<0 else (0, CMAX/2)
while queue:
    min_dis = MAX_INT
    for i,n in enumerate(queue):
        if dis[n] < min_dis:
            min_dis = dis[n]
            min_n = i
            now = n
    visited[now] = True
    for cost in costs[now]:
        next, dist = cost
        if visited[next]: continue
        queue.append(next)
        if dis[next]==MAX_INT or dis[now] + dist < dis[next]:
            dis[next] = dis[now] + dist
            parent[next] = now
            need[next] = need[now] - bikes[next]
            back[next] = back[now]
            if need[next] < 0:
                back[next] -= need[next]
                need[next] = 0
        elif dis[now] + dist == dis[next]:
            tmp = bikes[next] - CMAX/2
            n = need[now] - bikes[next]
            b = back[now]
            if n < 0:
                b -= n
                n = 0
            if n < need[next] or \
                (n == need[next] and b < back[next]):
                parent[next] = now
                need[next] = n
                back[next] = b

str = '0'
i = 0
while i!=sp:
    i = parent[i]
    str += '->%d' % i
print need[0], str, back[0]
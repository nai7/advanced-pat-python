from copy import copy
line_input = lambda: map(int, raw_input().split())
N, M, S, D = line_input()
matrix = [{} for n in xrange(N)]
add_highway = lambda c1, c2, dis, cst: \
    (matrix[c1].setdefault(c2, (dis, cst)),
    matrix[c2].setdefault(c1, (dis, cst)))
[add_highway(*line_input()) for m in xrange(M)]

dist = lambda c1, c2: matrix[c1][c2][0]
cost = lambda c1, c2: matrix[c1][c2][1]
def calculate(func, path):
    sum = 0
    for i in xrange(len(path)-1):
        sum += func(path[i], path[i+1])
    return sum

sh_path = None
sh_sum_dist = 0
sh_sum_cost = 0
def handle_path(path):
    global sh_path, sh_sum_dist, sh_sum_cost
    sum_dist = calculate(dist, path)
    sum_cost = calculate(cost, path)
    if (not sh_path) or \
        sum_dist < sh_sum_dist or \
        (sum_dist == sh_sum_dist and \
        sum_cost < sh_sum_cost):
        sh_sum_dist = sum_dist
        sh_sum_cost = sum_cost
        sh_path = copy(path)

path = [S]
def dfs(start):
    if start==D:
        handle_path(path)
    for city in matrix[start]:
        if not city in path:
            path.append(city)
            dfs(city)
            path.pop()

dfs(S)
for city in sh_path: print city,
print sh_sum_dist, sh_sum_cost
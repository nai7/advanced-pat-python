# won't pass test point 4, for running out of time
# you may rewrite it in C/C++ to pass this
N, M, K = map(int, raw_input().split())
mat = [[0]*(N+1) for i in xrange(N+1)]
for m in xrange(M):
    A, B = map(int, raw_input().split())
    mat[A][B] = mat[B][A] = 1

def DFS(mat, start, need_vst):
    need_vst[start] = False
    for next in xrange(1,N+1):
        if need_vst[next] and mat[start][next]:
            DFS(mat, next, need_vst)

for q in map(int, raw_input().split()):
    cnt = -1
    need_vst = [True]*(N+1)
    need_vst[0] = need_vst[q] = False
    for i in xrange(1,N+1):
        if need_vst[i]:
            DFS(mat, i, need_vst)
            cnt += 1
    print cnt
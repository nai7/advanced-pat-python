circle = map(int, raw_input().split())
N = circle[0]
circle[0] = 0
for i in xrange(1, N+1):
    circle[i] += circle[i-1]
Q = input()
for q in xrange(Q):
    beg, end = map(int, raw_input().split())
    beg, end = (beg, end) if end > beg else (end, beg)
    length = circle[end-1] - circle[beg-1]
    print min(length, circle[N] - length)
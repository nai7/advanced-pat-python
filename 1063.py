from __future__ import division
N = input()
sets = []
for i in xrange(N):
    s = map(int, raw_input().split())
    s.pop(0)
    sets.append(set(s))
Q = input()
for q in xrange(Q):
    i1, i2 = map(int, raw_input().split())
    i1, i2 = i1 - 1, i2 - 1
    s1, s2 = sets[i1], sets[i2]
    s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    Nc = 0
    for n in s1:
        if n in s2:
            Nc += 1
    Nt = len(s1) + len(s2) - Nc
    print '%.1f%%' % ((Nc / Nt) * 100)

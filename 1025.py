N = input()
ranklist = []
for n in xrange(N):
    cnt = input()
    for i in xrange(cnt):
        entry = raw_input().split()
        entry[-1] = int(entry[-1])
        entry.append(n+1)
        ranklist.append(entry)

print len(ranklist)
def mcmp(a1, a2):
    if a1[1] != a2[1]:
        return cmp(a2[1], a1[1])
    else:
        return cmp(a1[0], a2[0])
ranklist.sort(mcmp)

ranks = [0] * (N+1)
eqcnt = [0] * (N+1)
lasts = [-1] * (N+1)
for entry in ranklist:
    score = entry[1]
    for loc in 0, entry[-1]:
        if score == lasts[loc]:
            eqcnt[loc] += 1
        else:
            ranks[loc] += 1 + eqcnt[loc]
            eqcnt[loc] = 0
            lasts[loc] = score
    print entry[0], ranks[0], loc, ranks[loc]
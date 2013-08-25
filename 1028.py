N, C = map(int, raw_input().split())
C -= 1
records = [raw_input().split() for i in xrange(N)]
def mcmp(a1, a2):
    if a1[C] == a2[C]:
        return cmp(a1[0], a2[0])
    else:
        return cmp(a1[C], a2[C])
records.sort(mcmp)
for record in records:
    for col in record:
        print col,
    print
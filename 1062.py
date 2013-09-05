N, L, H = map(int, raw_input().split())
sages = []
noblemen = []
foolmen = []
smallmen = []
cnt = 0
for i in xrange(N):
    id, v, t = raw_input().split()
    v, t = map(int, (v, t))
    if v < L or t < L: continue
    if v >= H and t >= H:
        sages.append((id, v, t))
    elif v >= H:
        noblemen.append((id ,v, t))
    elif t < H and v >= t:
        foolmen.append((id, v, t))
    else:
        smallmen.append((id, v, t))
    cnt += 1

print cnt

def mcmp(p1, p2):
    if sum(p1[1:])==sum(p2[1:]):
        if p1[1]==p2[1]:
            return cmp(p1[0], p2[0])
        else:
            return cmp(p2[1], p1[1])
    else:
        return cmp(sum(p2[1:]), sum(p1[1:]))

for people in sages, noblemen, foolmen, smallmen:
    for p in sorted(people, mcmp):
        print p[0], p[1], p[2]
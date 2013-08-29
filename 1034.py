N, K = map(int, raw_input().split())
mmap = {}
for i in range(N):
    a, b, m = raw_input().split()
    mmap.setdefault(a, {}).setdefault(b, [0])[0] += int(m)
    mmap.setdefault(b, {}).setdefault(a, [0])[0] += int(m)

def dfs(start, gang):
    gang.append(start)
    for name in mmap[start]:
        if name not in gang:
            dfs(name, gang)
    return gang

def check_gang(gang):
    total_sum = 0
    max_sum = -1
    for name in gang:
        sum = 0
        for tname in mmap[name]:
            sum += mmap[name][tname][0]
        if max_sum == -1 or sum > max_sum:
            max_sum = sum
            head = name
        total_sum += sum
    if total_sum / 2 > K:
        return head
gangs = []
vsted = []
for name in mmap:
    if name in vsted: continue
    gang = dfs(name, [])
    vsted += gang
    if len(gang) < 3: continue
    head = check_gang(gang)
    if head:
        gangs.append((head, len(gang)))

print len(gangs)
for gang in sorted(gangs, lambda a1, a2: cmp(a1[0], a2[0])):
    print gang[0], gang[1]
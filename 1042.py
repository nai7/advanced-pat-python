d = dict(zip('SHCDJ', (13,)*4+(2,)))
series = [c + str(i+1) for c in 'SHCDJ' for i in range(d[c])]
N = input()
nums = map(int, raw_input().split())
order = range(54)
for i in xrange(N):
    new_order = [0] * 54
    for j, n in enumerate(nums):
        new_order[n-1] = order[j]
    order = new_order
for i in order:
    print series[i],
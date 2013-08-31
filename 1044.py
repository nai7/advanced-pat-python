N, M = map(int, raw_input().split())
chain = map(int, raw_input().split())
def pay_options(chain, M):
    beg, cur = 0, 1
    sum = chain[beg]
    while cur < N:
        sum += chain[cur]
        while sum > M:
            sum -= chain[beg]
            beg += 1
        if sum == M:
            yield beg, cur
        cur += 1

have_solution = False
while not have_solution:
    for beg, end in pay_options(chain, M):
        print '%d-%d' % (beg+1, end+1)
        have_solution = True
    M += 1
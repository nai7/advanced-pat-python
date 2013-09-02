M, N = map(int, raw_input().split())
color_cnt = {}
for i in xrange(N):
    for color in raw_input().split():
        color_cnt.setdefault(color, [0])[0] += 1
        if color_cnt[color][0] > M * N / 2:
            print color
            break
N, K = map(int, raw_input().split())
customs = []
for n in xrange(N):
    customs.append(raw_input())

START_TIME = 8 * 3600
END_TIME = 17 * 3600
serverd = 0
windows = []
waittime = 0
for cus in sorted(customs):
    cus = cus.split()
    cus[0] = map(int, cus[0].split(':'))
    cus[1] = int(cus[1]) * 60
    cus[0] = cus[0][0]*3600 + cus[0][1]*60 + cus[0][2]
    if cus[0] > END_TIME:
        break
    serverd += 1
    if len(windows) < K:
        wait_until = START_TIME
    else:
        wait_until = min(windows)
        windows.remove(wait_until)
    waittime += wait_until - cus[0] if cus[0] < wait_until else 0
    windows.append(max(wait_until, cus[0]) + cus[1])
print '%.1f' % (waittime/(60.0*serverd))











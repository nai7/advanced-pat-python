stops = map(int,raw_input().split())
del stops[0]
curstop = 0
totaltime = 5 * len(stops)
for stop in stops:
    if stop > curstop:
        totaltime += 6 * (stop - curstop)
    else:
        totaltime += 4 * (curstop - stop)
    curstop = stop

print totaltime
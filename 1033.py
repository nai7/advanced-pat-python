from __future__ import division
cmax, dest, davg, N = map(int, raw_input().split())
str2value = lambda price, dis: (int(dis), float(price))
stations = [str2value(*raw_input().split()) for i in xrange(int(N))]
stations.sort(lambda a1, a2: cmp(a1[0], a2[0]))
stations.append((dest, -1))
if stations[0][0] > 0:
    print 'The maximum travel distance = 0.00'
    exit(0)

cur_gas = 0
cost = 0
cur_station = stations[0]
step = cmax * davg
while cur_station[0] < dest:
    next_station = None
    need_full = True
    for station in stations[stations.index(cur_station)+1:]:
        if station[0] - cur_station[0] > step: break
        if station[1] < cur_station[1]:
            next_station = station
            need_full = False
            break
        if not next_station or \
            station[1] < next_station[1]:
            next_station = station
    if not next_station:
        print 'The maximum travel distance = %.2f' \
              % (cur_station[0] + step)
        exit(0)
    need_gas = (next_station[0] - cur_station[0]) / davg
    cost += ((cmax if need_full else need_gas) - cur_gas) * cur_station[1]
    cur_gas = cmax - need_gas if need_full else 0
    cur_station = next_station

print '%.2f' % cost
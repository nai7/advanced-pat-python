tm2secs = lambda t: t[0] * 3600 + t[1] * 60 + t[2]
secs2tm = lambda s: '%02d:%02d:%02d' % (s/3600, s/60%60, s%60)
N = input()
players = [raw_input() for i in xrange(N)]
players.sort()
for i, player in enumerate(players):
    player = player.split()
    atime = tm2secs(map(int, player[0].split(':')))
    ptime, isvip = map(int, player[1:])
    if ptime > 120: ptime = 120
    players[i] = atime, ptime, isvip

N, M = map(int, raw_input().split())
vips = map(int, raw_input().split())
now = tm2secs((8,0,0))
create_table = lambda i: [0, True if i+1 in vips else False, now]
tables = [create_table(i) for i in xrange(N)]

def get_a_table(atime):
    for table in tables:
        if table[-1] <= atime:
            return table

def get_a_vip_table(atime):
    for table in tables:
        if table[-1] <= atime and table[1]:
            return table

def print_record(atime, stime):
    wtime = (stime - atime + 30) / 60
    atime = secs2tm(atime)
    stime = secs2tm(stime)
    print atime, stime, wtime

def serv_table(table, atime, ptime):
    table[0] += 1
    table[-1] = max(table[-1], atime)
    print_record(atime, table[-1])
    table[-1] += ptime * 60

def get_earliest_table():
    tmp = [table[-1] for table in tables]
    return tables[tmp.index(min(tmp))]

def get_a_vip_player(index, table):
    for player in players[index+1:]:
        if player[-1] and player[0] <= table[-1]:
            players.remove(player)
            players.insert(index, player)
            return player

for i, player in enumerate(players):
    atime, ptime, isvip = player
    if atime >= tm2secs((21, 0, 0)): break
    if isvip:
        vip_table = get_a_vip_table(atime)
        if vip_table:
            serv_table(vip_table, atime, ptime)
            continue
    table = get_a_table(atime)
    if table:
        serv_table(table, atime, ptime)
        continue
    else:
        table = get_earliest_table()
        if table[-1] >= tm2secs((21, 0, 0)): break
        if not isvip and table[1]:
            vip_player = get_a_vip_player(i, table)
            if vip_player:
                atime, ptime, isvip = vip_player
                serv_table(table, atime, ptime)
                continue
        serv_table(table, atime, ptime)

for table in tables:
    print table[0],
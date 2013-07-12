N, M, K, Q = map(int, raw_input().split())
rows = [[] for i in xrange(N)]
people = [[dur_time,dur_time] for dur_time in map(int, raw_input().split())]
for i, person in enumerate(people):
    if i < M*N:
        min_n = i % N
    else:
        out_times = [rows[n][0] for n in xrange(N)]
        min_n = out_times.index(min(out_times))
        rows[min_n].pop(0)
    if len(rows[min_n]):
        person[1] += rows[min_n][-1]
    rows[min_n].append(person[1])

questions = map(int, raw_input().split())
for q in questions:
    out_time = people[q-1][1]
    if out_time - people[q-1][0] >= (17-8)*60:
        print 'Sorry'
    else:
        print "%02d:%02d" % (out_time/60 + 8, out_time%60)


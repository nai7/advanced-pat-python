N, Q = map(int, raw_input().split())
stu = {}
courses = ['A', 'C', 'M', 'E']
for n in range(N):
    input = raw_input().split();
    ID = input[0]
    input[1:] = map(int, input[1:])
    input[0] = (sum(input[1:])/3)
    stu[ID] = [input[i] for i in range(4)]

for i in range(Q):
    me = stu.get(raw_input())
    if not me:
        print 'N/A'
    else:
        rank = [1 for i in range(4)]
        for other in stu.values():
            if other is not me:
                for i in range(4):
                    if other[i] > me[i]:
                        rank[i] += 1
        minr = rank[0]
        mini = 0
        for i,r in enumerate(rank[1:]):
            if r < minr:
                minr = r
                mini = i + 1
        print minr, courses[mini]
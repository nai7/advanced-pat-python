NS, NC = map(int, raw_input().split())
courses = [[] for i in xrange(NC)]
names = []
for i in xrange(NS):
    stu = raw_input().split()
    name = stu.pop(0)
    names.append(name)
    N = stu.pop(0)
    course = map(int, stu)
    for c in course:
        courses[c-1].append(name)
for i, c  in enumerate(courses):
    print i+1, len(c)
    for name in sorted(names):
        if name in c:
            print name
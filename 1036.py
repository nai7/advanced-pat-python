N = input()
boys = []
girls = []
for i in xrange(N):
    name, sex, id, grade = raw_input().split()
    if sex == 'F':
        girls.append((name, id, int(grade)))
    else:
        boys.append((name, id, int(grade)))

girl_max = -1
if girls:
    for girl in sorted(girls, lambda a1, a2: cmp(a2[-1], a1[-1])):
        girl_max = girl[-1]
        print girl[0], girl[1]
        break
else:
    print 'Absent'

boy_min = -1
if boys:
    for boy in sorted(boys, lambda a1, a2: cmp(a1[-1], a2[-1])):
        boy_min = boy[-1]
        print boy[0], boy[1]
        break
else:
    print 'Absent'

if boy_min==-1 or girl_max==-1:
    print 'NA'
else:
    print girl_max - boy_min
costs = map(int, raw_input().split())
N = input()
calls = []
for n in xrange(N):
    calls.append(raw_input())

bills = {}
for call in sorted(calls):
    call = call.split()
    bill = bills.get(call[0])
    if not bill:
        bills[call[0]] = bill = []
    bill.append(call[1:])

for name in bills:
    month = bills[name][0][0][0:2]
    break

for name in bills:
    left = -1
    useful_bills = []
    for i,call in enumerate(bills[name]):
        if call[1] == 'on-line':
            left = i
        elif left != -1:
            useful_bills.append((bills[name][left][0][3:],
                                 bills[name][i][0][3:]))
            left = -1
    bills[name] = useful_bills

def getCost(startTime,endTime):
    startTime = map(int, startTime.split(':'))
    endTime = map(int, endTime.split(':'))
    cost = 0
    summin = 0
    while startTime[0] < endTime[0]:
        if startTime[2]!=0:
            cost += costs[startTime[1]] * (60 - startTime[2])
            summin += 60 - startTime[2]
            startTime[2] = 0
            startTime[1] += 1
        for h in range(startTime[1],24):
            cost += costs[h] * 60
            summin += 60
        startTime[0] += 1
        startTime[1:] = 0,0
    while startTime[1] < endTime[1]:
        if startTime[2]!=0:
            cost += costs[startTime[1]] * (60 - startTime[2])
            summin += 60 - startTime[2]
            startTime[2] = 0
            startTime[1] += 1
        else:
            cost += costs[startTime[1]] * 60
            summin += 60
            startTime[1] += 1
    cost += costs[startTime[1]] * (endTime[2] - startTime[2])
    summin += endTime[2] - startTime[2]
    return summin, float(cost)/100

for name in sorted(bills):
    if not bills[name]:
        continue
    print name,month
    sumcost = 0
    for record in bills[name]:
        summin, cost = getCost(record[0],record[1])
        print record[0],record[1],summin,'$%.2f' % cost
        sumcost += cost
    print 'Total amount: $%.2f' % sumcost
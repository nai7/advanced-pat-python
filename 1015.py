while True:
    str = raw_input()
    str = str.split()
    num = int(str[0])
    if num < 0:
        break
    redix = int(str[1])

    tmp = num
    numr = 0
    while tmp > 0:
        numr *= redix
        numr += tmp % redix
        tmp /= redix
    isPrime = True
    if num == 0 or num == 1:
        isPrime = False
    if numr == 0 or numr == 1:
        isPrime = False
    for i in xrange(2,num):
        if num % i == 0:
            isPrime = False
    for i in xrange(2,numr):
        if numr % i == 0:
            isPrime = False
    if isPrime == True:
        print 'Yes'
    else:
        print 'No'

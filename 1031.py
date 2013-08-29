s = raw_input()
h = (len(s) + 2) / 3
w = len(s) - 2 * h
for i in xrange(h-1):
    print s[i] + ' '*w + s[-1-i]
print s[i+1:-1-i]
input()
favorite = map(int ,raw_input().split()[1:])
favorite = dict(zip(favorite, range(len(favorite))))
colors = map(int, raw_input().split()[1:])
stripe = []
for color in colors:
    if color in favorite:
        stripe.append(favorite[color])
N = len(stripe)
if N==0:
    print 0
else:
    length = [1] * N
    for i in xrange(1, N):
        for j in xrange(i):
            if stripe[i] >= stripe[j]:
                length[i] = max(length[i], length[j]+1)
    print max(length)
res = {}
for i in range(2):
    poly = raw_input().split()
    for i in range(int(poly[0])):
        key = int(poly[2*i+1])
        value = float(poly[2*i+2])
        if res.has_key(key)1:
            res[key] += value
            if abs(res[key]) < 0.01:
                res.pop(key)
        else:
            res[key] = value

print len(res),
for i in range(len(res)):
    m = max(res.keys())
    print "%d %.1f" % (m,res.pop(m)),

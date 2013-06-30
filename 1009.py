poly1 = map(float,raw_input().split())
poly2 = map(float,raw_input().split())
del poly1[0],poly2[0]
res1 = {}
for i,x in enumerate(poly1[0:-1:2]):
    res1[int(x)] = poly1[i*2+1]

res = {}
for i,x in enumerate(poly2[0:-1:2]):
    for k in res1:
        res.setdefault(int(x)+k,0)
        res[int(x) + k] += poly2[i*2+1] * res1[k]

for k in res.keys():
    if abs(res[k]) < 5e-2:
        del res[k]
        
print len(res),
if not res: print 0, '%.1f' % 0.0
while res:
    k = max(res)
    print k,'%.1f' % res[k],
    del res[k]

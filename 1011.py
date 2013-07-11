res = 1
strs = ['W','T','L']
for i in range(3):
    input = map(float,raw_input().split())
    res *= max(input)
    print strs[input.index(max(input))],
print '%.2f' % ((res * 0.65 - 1) * 2)
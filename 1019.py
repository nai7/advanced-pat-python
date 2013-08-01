N, b = map(int, raw_input().split())
list = [N % b]
N /= b
while N:
    list.append(N % b)
    N /= b
length = len(list)
for k in range(length / 2):
    if list[k] != list[length-1-k]:
        print 'No'
        break
else:
    print 'Yes'

for n in reversed(list):
    print n,
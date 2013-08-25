lst1 = raw_input().split()
N1 = int(lst1.pop(0))
lst2 = raw_input().split()
N2 = int(lst2.pop(0))
N = N1 + N2
N = N/2 if N % 2 == 0 else N/2 + 1
i1 = i2 = 0
for i in range(N):
    if i1 >= N1:
        res = lst2[i2]
        i2 += 1
    elif i2 >= N2:
        res = lst1[i1]
        i1 += 1
    elif int(lst1[i1]) < int(lst2[i2]):
        res = lst1[i1]
        i1 += 1
    else:
        res = lst2[i2]
        i2 += 1
print int(res)
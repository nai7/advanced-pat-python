nums = set()
unique = []
for n in map(int, raw_input().split()[1:]):
    if n in nums:
        if n in unique:
            unique.remove(n)
    else:
        unique.append(n)
    nums.add(n)
if unique:
    print unique[0]
else:
    print 'None'
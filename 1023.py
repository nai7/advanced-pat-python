num = raw_input()
nums_before = {}
for n in num:
    nums_before.setdefault(n, []).append(0)
num = str(2 * int(num))
nums_after = {}
for n in num:
    nums_after.setdefault(n, []).append(0)

if nums_after == nums_before:
    print 'Yes'
else:
    print 'No'
print num
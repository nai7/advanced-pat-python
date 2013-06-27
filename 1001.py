nums = raw_input()
nums = nums.split()
res = int(nums[0])+int(nums[1])
isNeg = False
if res < 0:
    isNeg = True
    res = -res
res = str(res)
res = list(res)
res.reverse()
for i in xrange((len(res)-1)/3):
    res.insert((i+1)*3+i,',')
res.reverse()
res = ''.join(res)
if isNeg:
    res = '-' + res
print res

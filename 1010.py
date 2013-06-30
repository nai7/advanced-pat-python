nums = raw_input().split()
if nums[2]=='2':
    nums[0:2] = nums[1::-1]
radix1 = int(nums[3])
num1, num2 = nums[0:2]

def parseToInt(n):
    if 'a' <= n <= 'z':
        n = 10 + ord(n) - ord('a')
    else:
        n = int(n)
    return n

def todecimal(num, radix):
    res = 0
    for n in num:
        res *= radix
        res += parseToInt(n)
    return res

N1 = todecimal(num1, radix1)

low = parseToInt(max(num2)) + 1
high = N1 + 1

while high >= low:
    mid = (high + low) / 2
    N2 = todecimal(num2, mid)
    if N2 == N1:
        print mid
        break
    elif N2 > N1:                
        high = mid - 1        
    else:
        low = mid + 1
else: print 'Impossible'

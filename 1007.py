cnt = input()
num = map(int,raw_input().split())
curstart = 0
for x in num:
    if x < 0:
        curstart += 1
    else:
        break
if curstart == len(num):
    maxsum = maxstart = 0
    maxend = len(num) - 1
else:
    maxstart = maxend = curstart
    maxsum = cursum = num[curstart]
    curend = curstart
    for x in num[curstart+1:]:
        curend += 1
        if x < 0 or curend == len(num) - 1:
            if cursum > maxsum:
                maxsum = cursum
                maxstart = curstart
                maxend = curend - 1
        cursum += x
        if cursum < 0:
            curstart = curend + 1
            cursum = 0

print maxsum,num[maxstart],num[maxend]

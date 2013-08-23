num, max_step = map(int, raw_input().split())
def isPalindromic(snum):
    for i in xrange(len(snum)/2):
        if not snum[i] == snum[-i-1]:
            return False
    return True

step = 0
while not isPalindromic(str(num)):
    num = num + int(''.join(list(reversed(str(num)))))
    step += 1
    if step >= max_step:
        break
print num
print step
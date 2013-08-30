def is_symmetric(s):
    for i in xrange(len(s)/2):
        if not s[i] == s[-1-i]:
            return False
    return True

s = raw_input()
max_len = 1
for i, c in enumerate(s):
    j = s.rfind(c, i+1)
    while j > i:
        if is_symmetric(s[i:j+1]):
            length = j + 1 - i
            if length > max_len:
                max_len = length
            break
        else:
            j = s.rfind(c, i+1, j)

print max_len
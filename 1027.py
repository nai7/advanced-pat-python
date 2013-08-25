base = list('0123456789ABC')
def dec213(num):
    num = int(num)
    result = []
    while num:
        result.append(base[num % 13])
        num /= 13
    while len(result) < 2:
        result.append('0')
    return ''.join(reversed(result))
R, G, B = map(dec213, raw_input().split())
print '#%s%s%s' % (R, G, B)
cnt = input()
record = {}
for i in range(cnt):
    s = raw_input().split()
    record[s[0]] = s[1:]

first = last = record.popitem()
for i,t in record.items():
    if t[0] < first[1][0]:
        first = (i,t)
    if t[1] > last[1][1]:
        last = (i,t)

print first[0],last[0]

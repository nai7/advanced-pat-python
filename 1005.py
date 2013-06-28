num = list(raw_input())
num = map(int,num)
num = map(int,list(str(sum(num))))
num_names ='zero one two three four five six seven eight nine'.split()
for i in num:
    print num_names[i],

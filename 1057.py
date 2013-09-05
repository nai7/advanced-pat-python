stack = []
for i in xrange(input()):
    cmd = raw_input()
    if cmd[:3] == 'Pop':
        if not stack:
            print 'Invalid'
        else:
            print stack.pop(0)
    elif cmd[:3] == 'Pee':
        if not stack:
            print 'Invalid'
        else:
            print sorted(stack)[(len(stack)+1)/2-1]
    else:
        stack.insert(0, int(cmd.split()[1]))
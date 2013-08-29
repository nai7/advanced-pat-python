from string import maketrans
FROM = '10lO'
TO = '@%Lo'
TABLE = maketrans(FROM, TO)
def need_modify(s):
    for c in FROM:
        if c in s:
            return True
    return False

N = input()
accounts = [raw_input().split() for i in xrange(N)]
modified_accounts = []
for username, password in accounts:
    if need_modify(password):
        password = password.translate(TABLE)
        modified_accounts.append((username,password))
if modified_accounts:
    print len(modified_accounts)
    for username, password in modified_accounts:
        print username, password
else:
    if N == 1:
        print 'There is 1 account and no account is modified'
    else:
        print 'There are %d accounts and no account is modified' % N
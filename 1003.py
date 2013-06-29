def toInt(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

s = toInt(raw_input().split())
nCity,nRoad,cur,dst = s

nHelp = toInt(raw_input().split())

mmap = [[0]*nCity for i in range(nCity)]

for i in range(nRoad):
    road = toInt(raw_input().split())
    mmap[road[0]][road[1]] = road[2]
    mmap[road[1]][road[0]] = road[2]

vst = [False]*nCity
shtLen = 0
shtCnt = 0
maxHelp = 0

def shtPath(cur,curLen,curHelp):
    global dst,mmap,nCity,nHelp,vst,shtLen,shtCnt,maxHelp
    if shtLen!=0 and curLen > shtLen:
        return
    if cur==dst:
        if shtLen == 0:
            maxHelp = curHelp
            shtLen = curLen
            shtCnt = 1
        elif curLen == shtLen:
            if curHelp > maxHelp:
                maxHelp = curHelp
            shtCnt += 1
        elif curLen < shtLen:
            maxHelp = curHelp
            shtLen = curLen
            shtCnt = 1
    else:
        for d in range(nCity):
            if not vst[d] and mmap[cur][d]!=0:
                vst[d] = True
                curLen += mmap[cur][d]
                curHelp += nHelp[d]
                shtPath(d,curLen,curHelp)
                vst[d] = False
                curLen -= mmap[cur][d]
                curHelp -= nHelp[d]

vst[cur] = True
curLen = 0
curHelp = nHelp[cur]
shtPath(cur,curLen,curHelp)

print shtCnt,maxHelp

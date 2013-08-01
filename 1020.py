N = input()
post_order = map(int, raw_input().split())
in_order = map(int, raw_input().split())
import Queue
q = Queue.Queue()
q.put((post_order,in_order))
while not q.empty():
    p, i = q.get()
    if p and i:
        print p[-1],
        pos = i.index(p[-1])
        q.put((p[:pos], i[:pos]))
        q.put((p[pos:-1], i[pos+1:]))
from queue import *

def ver_tipo(ehQ, ehL, ehP):
        if ehQ and not ehL and not ehP:
            return "queue"
        elif ehL and not ehQ and not ehP:
            return "stack"
        elif ehP and not ehQ and not ehL:
            return "priority queue"
        elif ehQ and ehL or ehQ and ehP or ehL and ehP:
            return "not sure"
        return "impossible"

while True:
    try:
        e = int(input())
        q = Queue()
        l = LifoQueue()
        p = PriorityQueue()
        ehQ = True
        ehL = True
        ehP = True
        if e == "abc": break
        for i in range(e):
            o, n = map(int, input().split())
            if o == 1:
                q.put(n)
                l.put(n)
                p.put(-n)
            else:
                g = q.get()
                if ehQ and g == n:
                    ehQ = True
                else:
                    ehQ = False

                g = l.get()
                if ehL and g == n:
                    ehL = True
                else:
                    ehL = False

                g = abs(p.get())
                if ehP and g == n:
                    ehP = True
                else:
                    ehP = False
        print(ver_tipo(ehQ, ehL, ehP))
    except EOFError:
        break

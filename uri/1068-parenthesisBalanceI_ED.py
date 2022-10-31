from collections import deque
while True:
    try:
        e = input()
        d = deque()
        for i in e:
            if i == "(":
                d.append(i)
            elif i == ")":
                d.pop()
        if len(d) == 0:
            print("correct")
        else:
            print("incorrect")
    except IndexError:
        print("incorrect")
    except EOFError:
        break

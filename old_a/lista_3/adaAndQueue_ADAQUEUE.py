from collections import deque


num = int(input())
d = deque()
reverse = 0
for i in range(num):
    com = input().split()
    dado = com[0]
    try:
        if reverse%2 == 0:
            if dado == "toFront":
                d.append(com[1])
            elif dado == "push_back":
                d.appendleft(com[1])
            elif dado == "back":
                print(d.popleft())
            elif dado == "front":
                print(d.pop())
            else:
                reverse += 1
        else:
            if dado == "toFront":
                d.appendleft(com[1])
            elif dado == "push_back":
                d.append(com[1])
            elif dado == "back":
                print(d.pop())
            elif dado == "front":
                print(d.popleft())
            else:
                reverse += 1
    except IndexError:
        print("No job for Ada?")

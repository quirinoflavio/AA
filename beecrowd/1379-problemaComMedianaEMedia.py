a, b = map(int, raw_input().split())

while(a != 0):
    print(min(a, b)*3-(a+b))

    a, b = map(int, raw_input().split())
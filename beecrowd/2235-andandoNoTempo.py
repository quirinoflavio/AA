a, b, c = map(int, raw_input().split())

if(a == b or a == c or b == c or a == (b+c) or b == (a+c) or c == (b+a)):
    print("S")
else:
    print("N")
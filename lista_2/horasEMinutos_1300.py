while True:
    try:
        a = int(input())
        print("Y") if a%6==0 else print("N")
    except EOFError:
        break

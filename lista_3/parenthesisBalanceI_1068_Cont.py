while True:
    try:
        es = 0
        di = 0
        d = input()
        for p in d:
            if p == "(":
                es += 1
            elif p == ")":
                di += 1
            if di > es:
                print("incorrect")
                break
        if es == di:
            print("correct")
        elif es > di:
            print("incorrect")
    except EOFError:
        break

while True:
    try:
        t = input()
        i = 0
        meio = ""
        inicio = []
        fim = ""
        while i < len(t):
            if t[i] == "[":
                x = i+1
                temp = ""
                while x < len(t) and t[x] not in "[]" :
                    temp += t[x]
                    x += 1
                inicio.append(temp)
                i = x
            elif t[i] == "]":
                x = i+1
                temp = ""
                while x < len(t) and t[x] not in "[]" :
                    temp += t[x]
                    x += 1
                fim += temp
                i = x
            else:
                meio += t[i]
                i += 1
        saida = ""
        for i in range(len(inicio)-1, -1, -1):
            saida += inicio[i]
        saida += meio
        saida += fim
        print(saida)
    except EOFError:
        break

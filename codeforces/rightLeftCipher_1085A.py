word = raw_input()

right = False
if len(word)%2 == 0: right = True

nw = ""
while word != "":
    if right:
        nw = nw + word[-1]
        word = word[:-1]
        right = False
    else:
        nw = nw + word[0]
        word = word[1:]
        right = True

print nw[::-1]
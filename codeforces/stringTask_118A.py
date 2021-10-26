string = input().lower()

vogal = ["a", "e", "i", "o", "u", "y"]

s2 = ""

for s in string:
    if s not in vogal:
        s2 += ("." + s)

print (s2)

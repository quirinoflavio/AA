t, d, m = map(int, input().split())

dormi = False
if m == 0: dormi = True

ant = 0

for i in range(m):
    r = int(input())
    if abs(ant - r) >= t:
        dormi = True
    ant = r

if abs(ant - d) >= t:

    dormi = True

if t > d: dormi = False
print("Y" if dormi else "N")

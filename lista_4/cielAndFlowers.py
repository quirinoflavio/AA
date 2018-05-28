T=3
total = 0
i = 0
r,g,b=map(int,input().split())


if (r%T==2 and g%T==2) or (r%T==2 and b%T==2) or (g%T==2 and b%T==2):
    while r > 0 and g > 0 and b > 0 and i < 2:
        total+=1;r-=1;g-=1;b-=1
        i+=1
    total+=(r//3);r-=(r//3)
    total+=(g//3);r-=(g//3)
    total+=(b//3);b-=(b//3)

else:
    total+=(r//3);r-=(r//3)*3
    total+=(g//3);g-=(g//3)*3
    total+=(b//3);b-=(b//3)*3
    while r > 0 and g > 0 and b > 0:
        total+=1;r-=1;g-=1;b-=1
print(total)

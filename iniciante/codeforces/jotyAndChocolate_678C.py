def mmc(a,b): #mmc(a,b)*mdc(a,b)=a*b
    n1=a
    n2=b

    r = None
    while r != 0:
        r = n1%n2
        n1= n2
        n2 = r

    return (a*b)//n1


n,a,b,p,q=map(int, input().split())

result =  (n//a)*p
result += (n//b)*q

result -= (n//mmc(a,b))*min(p,q)

print(result)

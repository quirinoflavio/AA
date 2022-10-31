def gcd(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

n = int(raw_input())
i = 0



while (i < n):
    a = int(raw_input(), 2)
    b = int(raw_input(), 2)

    if gcd(a, b) != 1 : print ("Pair #%s: All you need is love!" % str(i+1))
    else: print ("Pair #%s: Love is not all you need!" % str(i+1))
    i+=1
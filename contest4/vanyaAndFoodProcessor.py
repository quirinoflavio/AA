n, h, k = map(int, raw_input().split())

potatos = map(int, raw_input().split())

usado = 0
counter = 0

p = 0
while p < len(potatos)-1:
    print p, counter , usado
    if potatos[p] + usado <= h:
        usado += potatos[p]
        if potatos[p+1] + usado > h:
            if k > usado: 
                counter += 1
                usado = 0
            else:
                counter += usado / k
                usado = usado % k
        p += 1
        
    else:
        if k > usado: 
            counter += 1
            usado = 0
        else:
            counter += usado / k
            usado = usado % k

print counter
if potatos[-1] + usado <= h: 
    usado += potatos[-1]
    if k > usado: 
        counter += 1
        usado = 0
    else:
        counter += usado / k
        usado = usado % k
else:
    if k > usado: 
        counter += 1
        usado = 0
    else:
        counter += usado / k
        usado = usado % k
    usado += potatos[-1]
    if k > usado: 
        counter += 1
        usado = 0
    else:
        counter += usado / k
        usado = usado % k
        


print counter
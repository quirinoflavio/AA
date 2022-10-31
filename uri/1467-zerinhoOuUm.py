import math

while True:
    try:
        l = map(float, raw_input().split())
        zero = 0
        
        for i in xrange(len(l)):
            if(l[i] == 0):
                zero += 1
        
        if(zero == 0 or zero == 3):
            print("*")
        else:
            if(zero == 1):
                for i in xrange(len(l)):
                    if(l[i] == 0):
                        print(chr(65+i))
                        break
            else:
                for i in xrange(len(l)):
                    if(l[i] == 1):
                        print(chr(65+i))
                        break
    except EOFError:
        break
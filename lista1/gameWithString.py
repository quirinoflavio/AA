s = raw_input()

stack = list()
stack.append(s[0])
cnt = 0
for i in xrange(1, len(s)):
    if stack and s[i] == stack[-1]:
        stack.pop(-1)
        cnt += 1
    else:
        stack.append(s[i])

if cnt%2 == 0:
    print "No"
else:
    print "Yes"
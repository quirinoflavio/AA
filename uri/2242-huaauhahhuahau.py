s = raw_input()
ind = ""
vind = ""

for i in xrange(len(s)):
    if(s[i] in ("a", "e", "i", "o", "u")):
        ind += s[i]

for i in xrange(len(s)-1, -1, -1):
    if(s[i] in ("a", "e", "i", "o", "u")):
        vind += s[i]

if(ind == vind):
    print("S")
else:
    print("N")
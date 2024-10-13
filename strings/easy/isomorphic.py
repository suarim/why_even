s="paper"
t="title"
h={}
for i in range(len(s)):
    if s[i] not in h:
        h[s[i]]=t[i]
    else:
        if h[s[i]]!=t[i]:
            print(False)
            exit()
print(h)
print(True)
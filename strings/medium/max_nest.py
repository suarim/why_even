s="(((())))()"
maxs=0
chars=0
for i in s:
    if i=='(':
        chars+=1
        print(chars)
        maxs=max(chars,maxs)
    elif i==')':
        chars-=1
print(maxs)
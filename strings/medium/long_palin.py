s="xcababa"
longest=""

for i in range(len(s)):
    l=i
    r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>len(longest):
            longest=s[l:r+1]
        l-=1
        r+=1
    l=i
    r=i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>len(longest):
            longest=s[l:r+1]
        l-=1
        r+=1
print(longest)
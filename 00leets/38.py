n=4
ans='1'
def helper(s):
    res=''
    count=1
    for i in range(len(s)):
        if i==len(s)-1 or s[i]!=s[i+1]:
            res+=str(count)+s[i]
            count=1
        else:
            count+=1

    return res
for i in range(2,n+1):
    ans=helper(ans)
    print(ans)
print(ans)
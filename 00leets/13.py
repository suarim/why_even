map={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
s="VII"
s=s[::-1]
res=map[s[0]]
print(res)
for i in range(1,len(s)):
    if map[s[i]]<map[s[i-1]]:
        res-=map[s[i]]
    else:
        res+=map[s[i]]
print(res)

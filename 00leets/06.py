s="PAYPALISHIRING"
n=3
rows=[[] for i in range(n)]
x=0
d=1
for i in range(len(s)):
    rows[x].append(s[i])
    if x==0:
        d=1
    if x==n-1:
        d=-1
    x+=d
print(rows)
res=""
for i in rows:
    res+="".join(i)
print(res)

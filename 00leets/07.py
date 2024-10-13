
x=-123
if x<=-2**31 or x>=2**31-1:
    print( 0)
p=0
if x<0:
    p=1
    x*=-1
s=0
while(x!=0):
    r=x%10
    s=s*10+r
    x=x//10
if s<=-2**31 or s>=2**31-1:
    print( 0)
if p==1:
    print( s*-1)
else:
    print( s)

s="axc"
t="axbhc"
i=0
j=0
c=len(s)
while i<len(s) and j<len(t):
    if s[i]==t[j]:
        i+=1
    j+=1
if len(s)==i:
    print(True)
else:
    print(False)
    
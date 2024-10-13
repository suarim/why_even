s="  -042"
for i in s:
    print(s.index(i),i)
x=0
for i in s:
    if i==" ":
        x+=1
        continue
    else:
        break
print(x)
p=0
z=x
if s[x]=="-":
    x+=1
    p=1
while x<len(s) and s[x].isdigit():
    x+=1
print(int(s[z:x]))

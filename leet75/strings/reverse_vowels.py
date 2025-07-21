s = list("IceCreAm")
i=0
j=len(s)-1
while i<j:
    if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    elif s[i] in "aeiouAEIOU" and s[j] not in "aeiouAEIOU":
        j-=1
    else:
        i+=1

print("".join(s))
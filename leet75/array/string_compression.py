s=["a","a","b","b","b","b","b","b","b","b","b","b","b","b","b"]
i=0
r=0
while i<len(s):
    currentchar=s[i]
    current_occurence=0
    while((i<len(s)) and s[i]==currentchar):
        i+=1
        current_occurence+=1
    s[r]=currentchar
    r+=1
    if current_occurence>1:
        for p in str(current_occurence):
            s[r]=p
            r+=1
print(s[:])
s = "racecar"
t = "carrabe"
h1,h2={},{}
for i in s:
    if i in h1:
        h1[i]+=1
    else:
        h1[i]=1
for i in t:
    if i in h2:
        h2[i]+=1
    else:   
        h2[i]=1
print(h1==h2)
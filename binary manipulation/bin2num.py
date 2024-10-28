str="101"
res=0
k=0
for i in str[::-1]:
    res+=int(i)*2**k
    k+=1
print(res)
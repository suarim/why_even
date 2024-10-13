str="how are you my friend"
l=str.split()
print(" ".join(l[::-1]))


str="how are you my friend"
z=[]
k=len(str)
for i in range(len(str)-1,-1,-1):
    if str[i]==" ":
        z.append(str[i+1:k])
        k=i
z.append(str[0:k])
print(z)
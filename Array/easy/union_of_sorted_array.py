x=[1,1,2,3,4,5,6]
y=[2,3,4,5,6,7,8,9]
z=[]
i=0
j=0
while i<len(x) and j<len(y):
    if x[i]<=y[j]:
        z.append(x[i])
        i+=1
    else:
        z.append(y[j])
        j+=1
z.extend(x[i:])
z.extend(y[j:])
print(z)
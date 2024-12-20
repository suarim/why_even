l=[90,15,10,7,12,2]
n=len(l)
for i in range(n//2):
    left=2*i+1
    right=2*i+2
    if left<n and l[i]<l[left]:
        print(False)
        exit()
    if right<n and l[i]<l[right]:
        print(False)
        exit()
print(True)
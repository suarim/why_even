nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
res=[]
l=[]
r=[]
for i in nums1:
    if i not in nums2:
        l.append(i)
for i in nums2:
    if i not in nums1:
        r.append(i)
res.append(list(set(l)))
res.append(list(set(r)))
print(res)
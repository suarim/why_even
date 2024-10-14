s="((((()))))"
left=0
right=0
maxs=0
for i in s:
    if i=='(':
        left+=1
    else:
        right+=1
    if left==right:
        maxs=max(maxs,2*left)
    if right>left:
        left=right=0
left=right=0
for i in s[::-1]:
    if i=='(':
        left+=1
    else:
        right+=1
    if left==right:
        maxs=max(maxs,2*right)
    if left>right:
        left=right=0
print(maxs)
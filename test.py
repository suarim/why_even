l=[1,2,3]
res=[]
stack=[]
def dfs(i):
    if i>=len(l):
        res.append(stack[:])
        return
    stack.append(l[i])
    dfs(i+1)
    stack.pop()
    dfs(i+1)
dfs(0)
print(res)
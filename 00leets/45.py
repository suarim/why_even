l=[1,2,3]
stack=[]
res=[]
def dfs():
    if len(stack)==len(l):
        res.append(stack[:])
        return
    for i in l:
        if i in stack:
            continue
        stack.append(i)
        dfs()
        stack.pop()
dfs()
print(res)
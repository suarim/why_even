s="tree"
stack=[]
res=[]
def dfs(stack,lens):
    if len(stack)==lens:
        res.append(''.join(n for n, _ in stack))
        return
    for i,n in enumerate(s):
        if (n,i) not in stack:
            stack.append((n,i))
            dfs(stack,lens)
            stack.pop()
for i in range(1,5):
    dfs(stack,i)
print(res)

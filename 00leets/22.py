stack=[]
res=[]
n=3
def dfs(open,close):
    if open==n and close==n:
        res.append("".join(stack))
        return
    if open<n:
        stack.append("(")
        dfs(open+1,close)
        stack.pop()
    if close<open:
        stack.append(")")
        dfs(open,close+1)
        stack.pop()
dfs(0,0)
print(res)
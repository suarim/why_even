n=3
res=[]
stack=[]
def helper(open,close):
    if open==n and close==n:
        res.append(''.join(stack))
    if open<n:
        stack.append('(')
        helper(open+1,close)
        stack.pop()
    if close<open:
        stack.append(')')
        helper(open,close+1)
        stack.pop()
helper(0,0)
print(res)
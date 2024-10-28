arr = [2,3,6,7]
target = 7
res=[]
stack=[]
def dfs(i,total):
    if total==target:
        res.append(stack.copy())
        return
    if i>=len(arr) or total>target:
        return  
    stack.append(arr[i])
    dfs(i,total+arr[i])
    stack.pop()
    dfs(i+1,total)
dfs(0,0)
print(res)
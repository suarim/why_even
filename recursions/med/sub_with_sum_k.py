
def subsets(nums,k):
    res=set()
    stack=[]
    def dfs(i):
        if i>=len(nums):
            if sum(stack)==k:
                res.add(tuple(stack.copy()))
                return True
            else:
                return False
        stack.append(nums[i])
        if dfs(i+1):
            return True
        stack.pop()
        if dfs(i+1):
            return True
        return
    dfs(0)
    return res
print(subsets([1,2,1],3))

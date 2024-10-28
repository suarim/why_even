candidates = [2,3,6,7]
target = 7
def combinationSum(l, k):
    res=set()
    stack=[]
    def helper(i,sum):
        if sum==k:
            res.add(tuple(stack.copy()))
        if i>=len(l) or sum>k:
            return
        stack.append(l[i])
        helper(i,sum+l[i])
        stack.pop()
        helper(i+1,sum)
    helper(0,0)
    return res 
print(combinationSum(candidates,target)) # [[2, 2, 3], [7]]
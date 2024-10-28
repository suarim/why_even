candidates = [10,1,2,7,6,1,5]
target = 8
def combinationSum2(l, k):
    res=set()
    stack=[]
    def helper(i,sum):
        if sum==k:
            res.add(tuple(sorted(stack.copy())))
        if i>=len(l) or sum>k:
            return
        stack.append(l[i])
        helper(i+1,sum+l[i])
        stack.pop()
        helper(i+1,sum)
    helper(0,0)
    return res
print(combinationSum2(candidates,target)) # [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
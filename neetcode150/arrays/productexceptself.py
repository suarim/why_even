nums = [1,2,4,6]
presum=[1]
postsum=[1]
for i in range(len(nums)):
    postsum.append(postsum[-1]*nums[i])
print("postsum->",postsum)
for i in range(len(nums)-1,-1,-1):
    presum.insert(0,presum[0]*nums[i])
print("presum->",presum)
res=[]
for i in range(1,len(nums)+1):
    res.append(presum[i]*postsum[i-1])
print(res)
nums = [1,12,-5,-6,50,3]
k = 4
i=0
mavg=-9999
avg1=0
def average(nums1):
    return sum(nums1)/len(nums1)
while i+k<=len(nums):
    avg1=average(nums[i:i+k])
    mavg=max(mavg,avg1)
    i+=1
print(mavg)
import heapq
l=[]
arr=[1,2,3,4]
for i in arr:
    heapq.heappush(l,-i)
print([-x for x in l])
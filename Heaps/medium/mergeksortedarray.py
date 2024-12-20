import heapq
l=[[1,2,3],[4,5,6],[7,8,9]]
z=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        heapq.heappush(z,l[i][j])
print(z)
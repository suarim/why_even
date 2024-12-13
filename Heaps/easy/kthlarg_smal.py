import heapq
def larg_smal(l,k):
    z=[]
    for i in l:
        heapq.heappush(z,-i)
    j=0
    while j<k-1:
        heapq.heappop(z)
        j+=1
    y=[]
    for i in l:
        heapq.heappush(y,i)
    j=0
    while j<k-1:
        heapq.heappop(y)
        j+=1
    return -z[0],y[0]
print(larg_smal([3,2,1,5,6,4],3)) # 5

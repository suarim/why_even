intervals = [[1,4],[4,5]]
res=[intervals[0]]
for i in range(1,len(intervals)):
    last=res[-1][1]
    if intervals[i][0]<=last:
        res[-1][1]=max(last,intervals[i][1])
    else:
        res.append(intervals[i])
print(res)
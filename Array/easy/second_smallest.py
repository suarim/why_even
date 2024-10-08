import heapq
l=[5,6,7,3,6,121,90,3,2,-10]

sorted_array = sorted(l)
print(sorted_array[1])
#O(n log n)

sms=99999
min=99999
for i in l:
    if i<min:
        sms=min
        min=i
    if i<sms and i!=min:
        sms=i
print(sms)
#O(n)


heapq.heapify(l)
heapq.heappop(l)
print(heapq.heappop(l))
# Time Complexity: O(n) for heapify + O(log n) for each heappop, total O(n + 2*log n) = O(n) since log n is negligible compared to n

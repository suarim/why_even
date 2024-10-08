l=[1,2,3,4,5]
print(l[1:]+l[:1])
#O(n)

from collections import deque

l = deque([1, 2, 3, 4, 5])
l.append(l.popleft())  
print(list(l))  
#O(1)

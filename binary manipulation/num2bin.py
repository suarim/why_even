n=13
res=""
while n!=0:
    res+=str(n%2)
    n=n//2
print(res[::-1])
# time complexity: O(log(n))
# space complexity: O(log(n))
x=2.1
n=3
def helper(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if x==0:
        return 0
    res=helper(x,n//2)
    res=res*res
    return x*res if n%2==1 else res
print(helper(x,n))
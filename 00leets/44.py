s="aa"
p="*"
def check(i,j,dp):
    if i<0 and j<0:
        return True
    if i>=0 and j<0:
        return False
    if i<0 and j>=0:
        for x  in range(j+1):
            if p[x]!="*":
                return False
        return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==p[j] or p[j]=="?":
        dp[i][j]=check(i-1,j-1,dp)
        return dp[i][j]
    elif p[j]=="*":
        dp[i][j]=check(i-1,j,dp) or check(i,j-1,dp)
        return dp[i][j]
    else:
        return False
    
m=len(s)
n=len(p)
dp=[[-1 for _ in range(n)] for _ in range(m)]
print(dp)
print(check(m-1,n-1,dp))

s="racecar"
def palindrom(l,r):
    if s[l]!=s[r] :
        return False 
    if l>=r:
        return True
    return palindrom(l+1,r-1)
print(palindrom(0,len(s)-1))

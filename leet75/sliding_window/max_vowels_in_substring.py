s = "leetcode"
k = 3
i=0
maxc=-9999
c=0
def countvows(str):
    c=0
    for i in str:
        if i in "aeiouAEIOU":
            c+=1
    return c
while i+k<=len(s):
    count=countvows(s[i:i+k])
    maxc=max(maxc,count)
    i+=1
print(maxc)

    
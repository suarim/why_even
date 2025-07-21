word1="ab"
word2="pqrs"
i=0
j=0
res=""
k=0
while i<len(word1) and j<len(word2):
    if k==0:
        res+=word1[i]
        k=1
        i+=1
    else:
        res+=word2[j]
        k=0
        j+=1
res+=word1[i:]
res+=word2[j:]
print(res)

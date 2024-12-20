import string
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
def check(bw,ew,wordlist):
    q=[]
    if ew not in wordlist:
        return 0
    q.append((bw,1))
    while q:
        w,l=q.pop(0)
        x=list(w)
        for i in range(len(x)):
            org=x[i]
            for j in string.ascii_lowercase:
                x[i]=j
                nww="".join(x)
                if nww==ew:
                    return l+1
                if nww in wordlist:
                    q.append((nww,l+1))
            x[i]=org
    return 0 
print(check(beginWord,endWord,wordList))
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res=[]
        numres=[]
        stack=[]
        numstack=[]
        def dfs():
            if len(stack)==len(words):
                res.append(stack[:])
                numres.append(numstack[:])
                return
            for i,n in enumerate(words):
                if n not in stack or i not in numstack:
                    stack.append(n)
                    numstack.append(i)
                    dfs()
                    stack.pop()
                    numstack.pop()

        dfs()
        z=[]
        for i in res:
            z.append("".join(i))
        k=set()
        print(z)
        for perm in z:
            start = 0  # Start searching from the beginning of the string
            while True:
                start = s.find(perm, start)  # Find the permutation in the string
                if start == -1:  # If no more occurrences are found, break the loop
                    break
                k.add(start)
               
                
                start += 1  # Move past the current index to find the next occurrence
        print(k)
        return list(k)
    
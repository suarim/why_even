def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y=x
        s=0
        while x!=0:
            r=x%10
            s=s*10+r
            x=x//10
        if s==y:
            return True
        else:
            return False

x=121
print(isPalindrome(x))
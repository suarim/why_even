num1 = "2"
num2 = "3"
def mul(num1,num2):
    def str2(s):
        res=0
        for i in s:
            res=res*10+ord(i)-ord('0')
        return res
    return str(str2(num1)*str2(num2))
print(mul(num1,num2))
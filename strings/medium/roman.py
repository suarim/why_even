map = {
    1000: "M", 
    900: "CM", 
    500: "D", 
    400: "CD",
    100: "C", 
    90: "XC", 
    50: "L", 
    40: "XL", 
    10: "X", 
    9: "IX", 
    5: "V", 
    4: "IV", 
    1: "I"
}
n=11
res=""
for key,val in map.items():
    while n>=key:
        res+=val
        n-=key
print(res)


l={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
s="VIII"
s=s[::-1]
res=l[s[0]]
for i in range(1,len(s)):
    if l[s[i]]<l[s[i-1]]:
        res-=l[s[i]]
    else:
        res+=l[s[i]]
print(res)
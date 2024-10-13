map={
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
n=8
res=""
for key,val in map.items():
    while n>=key:
        res+=val
        n-=key
print(res)
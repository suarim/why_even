def gcd(a,b):
    print(a,b)
    while b:
        a,b=b,a%b
    print(a)
    return a
x=gcd(len("ABABABABAB"),len("ABABA"))
print("ABABABABAB"[:x])
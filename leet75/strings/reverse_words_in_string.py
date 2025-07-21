s =  "  hello world  "
s=" ".join(s.strip().split()[::-1])
print(s)
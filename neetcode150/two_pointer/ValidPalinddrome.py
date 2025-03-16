s = "Was it a car or a cat I saw?"
for c in ",.?:;":
    s = s.replace(c, "")
l = s.lower().split()
print(l)
print("".join(l)=="".join(l)[::-1])
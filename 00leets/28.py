haystack = "hello"
needle = "ll"
for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)]==needle:
        print(i)
        exit()
print(-1)
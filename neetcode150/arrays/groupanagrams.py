from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]
h=defaultdict(list)
for i in strs:
    h[str(sorted(i))].append(i)
print(list(h.values()))
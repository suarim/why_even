from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = defaultdict(list)
for s in strs:
    z="".join(sorted(s))
    print(z)
    anagrams[z].append(s)
print(list(anagrams.values()))
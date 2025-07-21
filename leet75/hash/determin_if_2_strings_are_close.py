from collections import Counter
word1="cabbba"
word2="abbccc"
if len(word1)!=len(word2):
    print( False)
v1=Counter(word1)
v2=Counter(word2)
print(v1.values())
print(v2.values())
print( set(v1.keys())==set(v2.keys()) and sorted(v1.values()) == sorted(v2.values()))
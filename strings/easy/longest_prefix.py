l=["flower","flow","floight"]
min_len=len(l[0])
for i in l:
    min_len=min(min_len,len(i))
print(min_len)

for i in range(min_len):
    for str in l:
        if l[0][i]!=str[i]:
            print(l[0][:i])
            exit()
print(l[0][:min_len])
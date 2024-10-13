strs = ["flower","flow","flight"]
min_len = min([len(s) for s in strs])
for i in range(min_len):
    for str in strs:
        if str[i]!=strs[0][i]:
            print(strs[0][:i])
            exit()
print(strs[0][:min_len])
    
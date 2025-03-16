l = [3, 4, 7, 1, 6, 7,2,3,2,97,-90]
sub=[]
for i in range(len(l)):
    b=l[i]
    if b==7:
        sub.append([b])
    for j in range(i+1,len(l)):
        b+=l[j]
        if b>7:
            break
        if b != 7:
            continue
        else:
            sub.append(l[i:j+1])
            break
mm=0
for i in sub:
    mm=max(mm,len(i))
print(sub)
print(mm)


l = [3, 4, 7, 1, 6, 7, 2, 3, 2, 97, -90]
prefixmap = {0: [-1]}  # Start with base case (sum 0 at index -1)
prefix = 0
target = 7
subarrays = []

for i, n in enumerate(l):
    prefix += n

    if (prefix - target) in prefixmap:  # Check if a subarray with sum=7 exists
        for start in prefixmap[prefix - target]:
            subarrays.append(l[start + 1:i + 1])  # Store the subarray

    # Store occurrences of each prefix sum
    if prefix in prefixmap:
        prefixmap[prefix].append(i)
    else:
        prefixmap[prefix] = [i]

print("All subarrays with sum 7:", subarrays)

arr = [3, 1, 5, 4, 2, 100, -90, 0]
for i in range(len(arr)):
    for j in range(i,0,-1):
        print(i)
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            print(f"{i},{j}->",arr)
        else:
            break
print(arr)
# O(n^2)
# Ω(n)
#works well for small data sets
# works well when the data set is almost sorted
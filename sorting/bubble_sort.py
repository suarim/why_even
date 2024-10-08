arr = [3, 1, 5, 4, 2, 100, -90, 0]
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):  
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

# O(n^2)
# Ω(n^2)
#works well for small data sets

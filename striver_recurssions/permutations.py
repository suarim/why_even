arr=['a','b','c']
def permute(arr, i):
    if i == len(arr):
        print(arr)
        return
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]   # swap
        permute(arr, i + 1)
        arr[i], arr[j] = arr[j], arr[i]   # swap back
permute(arr,0)
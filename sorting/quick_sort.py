def partitionn(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        p=partitionn(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

arr = [3, 1, 5, 4, 2, 100, -90, 0]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
# O(n^2)
# Ω(nlogn)
# works better than merge sort when the array is small
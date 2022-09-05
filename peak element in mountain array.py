def peak(arr):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end)//2
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid - 1
    return start
l = [1,7,6,4,2,1]
print(peak(l))
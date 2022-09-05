def swap (a,b,arr):
    arr[a],arr[b] = arr[b],arr[a]

def quicksort(start,end,arr):
    if start < end:
        pi = partition(start,end,arr)
        quicksort(start,pi-1,arr)
        quicksort(pi+1,end,arr)

def partition(start,end,arr):
    pivot_idx = start
    swap(pivot_idx,end,arr)
    for i in range(start,end):
        if arr[i] < arr[end]:
            swap(i,start,arr)
            start+=1
    swap(start,end,arr)
    return start

arr=[6,4,2,1,9,7]
quicksort(0,len(arr)-1,arr)
print(arr)
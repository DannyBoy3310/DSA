def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i-1
        while j>=0 and anchor<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = anchor

def find_median(arr):
    mid = len(arr)
    if mid%2==1:
        return arr[mid//2]
    else:
        return ((arr[mid//2])+(arr[(mid-1)//2]))/2

l = [2, 1, 5, 7, 2, 0, 5]
insertion_sort(l)
res = []
for el in l:
    res.append(el)
    insertion_sort(res)
    print(res)
    print(find_median(res))






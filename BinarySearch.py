def binarysearch(arr,key):
    start = 0
    end = len(arr)-1
    while (start <= end):
        mid = (start+end)//2
        if arr[mid]==key:
            return mid
        elif key > arr[mid]:
            start = mid+1
        else:
            end = mid - 1
    return -1
def find_repeateds(arr,key):
    index = binarysearch(arr,key)
    if index==-1:
        return "No element found"
    indices = [index]
    i = index-1
    while i>-0:
        if arr[i]==key:
            indices.append(i)
            i -= 1
        else:
            break
    i = index+1
    while (i<len(arr)):
        if arr[i]==key:
            indices.append(i)
            i+=1
        else:
            break
    return sorted(indices)
if __name__ == "__main__":
    l = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    print(find_repeateds(l,15))



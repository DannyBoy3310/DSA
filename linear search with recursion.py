def linear_search(arr,key):
    if len(arr)==0:
        return "Element not present"
    if arr[-1] == key:
        return len(arr)
    arr.pop(-1)
    res = linear_search(arr,key)
    return res
l = [4,6,1,9,87,23,46,82]
key = 23
print(linear_search(l,1))
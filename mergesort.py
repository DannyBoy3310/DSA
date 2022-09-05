# def merge_sort(arr,param,descending=False):
#     if len(arr)==1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid],param,descending)
#     right = merge_sort(arr[mid:],param,descending)
#     merged = merge(left,right,param,descending)
#     return merged
# def merge(left,right,param,descending):
#     res=[]
#     if descending is True:
#         i = len(left) - 1
#         j = len(right) - 1
#         res=[]
#         i = j = 0
#         res = []
#         while i < len(left) and j < len(right):
#             if left[i][param] > right[j][param]:
#                 res.append(left[i])
#                 i += 1
#             else:
#                 res.append(right[j])
#                 j += 1
#         while i < len(left):
#             res.append(left[i])
#             i += 1
#         while j < len(right):
#             res.append(right[j])
#             j += 1
#     else:
#         i=j=0
#         res =[]
#         while i < len(left) and j< len(right):
#             if left[i][param] < right[j][param]:
#                 res.append(left[i])
#                 i+=1
#             else:
#                 res.append(right[j])
#                 j+=1
#         while i< len(left):
#             res.append(left[i])
#             i+=1
#         while j < len(right):
#             res.append(right[j])
#             j+=1
#
#     return res
#
#
# if __name__=="__main__":
#     elements = [
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#     ]
#     print(merge_sort(elements,param="age",descending=True))

def mergesort(nums):
    if len(nums)==1:
        return nums
    mid = len(nums)//2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    merged = merge(left,right,nums)
    return merged

def merge(left,right,nums):
    i = j = k =0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k+=1
    while i < len(left):
        nums[k] = left[i]
        i+=1
        k+=1

    return nums

l =[-4,-1,0,3,10]
mergesort(l)
print(l)


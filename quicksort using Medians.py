def median_algo(nums, k):
    chunks = [nums[i:i+5] for i in range(0,len(nums),5)]
    medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
    pivot = sorted(medians)[len(medians)//2]
    left_Array = [n for n in nums if n < pivot]
    right_array = [m for m in nums if m > pivot]

    pivot_idx = len(left_Array)
    if k < pivot_idx:
        return median_algo(left_Array, k)
    elif k > pivot_idx:
        return median_algo(right_array, k-len(left_Array)-1)
    else:
        return pivot

def select(nums, k):
    return median_algo(nums, k-1)

list1 = [1, -5, 0, 10, 15, 20, 3, -1, 21, 22, 23, 24, 25, 26, 27, 28, 29]
pos = int(input())
print(select(list1,pos))
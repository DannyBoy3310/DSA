def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        pos_to_del = []
        for i in range(gap,n):
            anchor = arr[i]
            j = i
            while j >= gap and anchor <= arr[j-gap]:
                if anchor == arr[j-gap]:
                    pos_to_del.append(j)
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = anchor
        pos_to_del = sorted(set(pos_to_del))
        print(arr,pos_to_del,sep="\n")
        if pos_to_del:
            for i in pos_to_del[::-1]:
                del arr[i]
        n = len(arr)
        div*=2
        gap = n//div



if __name__=="__main__":
    elements = [21,98,29,11,17,4,25,11,32,9,29]
    shell_sort(elements)
    print(elements)
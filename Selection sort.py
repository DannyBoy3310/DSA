def selection_sort(arr):
    l= [*arr[0].keys()]
    print(l)
    for key in l[::-1]:
        for i in range(len(arr)-1):
            min_idx = i
            for j in range(i+1,len(arr)):
                if arr[j][key] < arr[min_idx][key]:
                    min_idx = j
            if min_idx != i:
                arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

if __name__=="__main__":
    ele = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
    print(*selection_sort(ele),sep="\n")
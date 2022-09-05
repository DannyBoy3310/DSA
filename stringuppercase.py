def uppercase(string,idx=0):
    res=''
    if string[idx].isupper():
        res+=uppercase(string,idx+1)
    if idx == len(string)-1:
        return "No uppercase"
    return string[idx]

str1="fudhuIIDUi9dhiue"
print(uppercase(str1))





#USING RECURSION
def mulitplication_recursion(a,b):
    if b==1:
        return a
    if b%2==0:
        return mulitplication_recursion(2*a,b//2)
    else:
        return a+mulitplication_recursion(2*a,b//2)

#USING ITERATION
def multiplication_iterative(a,b):
    res = 0
    while b > 0:
        if b ^ 1 == b-1:
            res = res+a
        a <<= 1
        b >>= 1
    return res

print(mulitplication_recursion(5,3))
print(multiplication_iterative(5,3))
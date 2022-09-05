def prime(num):
    c = 1
    for i in range(2, num):
        if num % i == 0:
            c += 1
    if c == 1:
        return True
    else:
        return False


def factors(num):
    l = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            l.append(i)
    return l


def nthUglyNumber(n: int) -> int:
    l = [1]
    i = 2
    while (len(l) != n):
        if i in [2, 3, 5]:
            l.append(i)
            i += 1
            continue
        elif prime(i):
            i+=1
            continue
        for val in factors(i):
            if prime(i):
                i += 1
                continue
        l.append(i)
        i += 1
        continue

    return l


n = 100
print(nthUglyNumber(11))
print(factors(14))
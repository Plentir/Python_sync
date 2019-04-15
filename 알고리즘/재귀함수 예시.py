def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def factorial(a):
    res = 1
    for i in range(2, a + 1):
        res *= i
    return res

print(fact(10))

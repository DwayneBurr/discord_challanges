def fib(n):
    s = []
    a, b = 0, 1
    for i in range(n + 1):
        # print(i)
        s.append(a)
        a, b = b, a + b
    return s
print(fib(8))
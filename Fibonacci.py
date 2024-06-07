def fibo(n):
    res = []
    a, b = 0, 1
    for i in range(n):
        res.append(a)
        a, b = b, a + b
    if len(res) > 1:
        res.pop(1)  # remove double occurence of 1 in list
    return res

n = 50
print(fibo(n))

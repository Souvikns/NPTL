# it runs until x is less in 1 and then return the value of d that is being incremented.
def f(x):
    d = 0
    while x > 1:
        (x, d) = (x / 5, d + 1)
        print((x, d))
    return d


# it returns the number of  factors n has except 1 and itself
def h(n):
    s = 0
    for i in range(2, n):
        if n % i == 0:
            s = s + 1
    return s


# It divides m with n and keeps on doing this until m is smaller than n then,
# it returns the number of times the loop ran
def g(m, n):
    res = 0
    while m >= n:
        (res, m) = (res + 1, m / n)
    return res


# It gives the answer of the following pattern
# 1+2+3+4+5+6+......n
# n*((n+1)/2)
def mys(m):
    if m == 1:
        return 1
    else:
        return m + mys(m - 1)

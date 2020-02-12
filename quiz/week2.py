# One of the following 10 statements generates an error.
# Which one? (Your answer should be a number between 1 and 10.)
def prob1():
    x = [1, "abcd", 2, "efgh", [3, 4]]  # Statement 1
    y = x[0:6]  # Statement 2
    z = x  # Statement 3
    w = y  # Statement 4
    x[1] = x[1][0:3] + 'd'  # Statement 5
    y[2] = 4  # Statement 6
    z[1][1:3] = 'yzw'  # Statement 7
    z[0] = 0  # Statement 8
    w[4][0] = 1000  # Statement 9
    a = (x[4][1] == 4)  # Statement 10


# Consider the following lines of Python code.
def prob2():
    x = [423, 'b', 37, 'f']
    u = x[1:]
    y = u
    w = x
    u = u[0:]
    u[1] = 53
    x[2] = 47


# What is the value of second after executing the following lines?
def prob3():
    first = "tarantula"
    second = ""
    for i in range(len(first) - 1, -1, -1):
        second = first[i] + second


# What is the value of list1 after the following lines are executed?

def mystery(l):
    l = l[0:5]
    return ()


if __name__ == '__main__':
    list1 = [44, 71, 12, 8, 23, 17, 16]
    mystery(list1)
    print(list1)

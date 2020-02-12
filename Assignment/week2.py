# to check whether a number can be expressed as the sum of three squares
import math


def isSquare(n: int):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


def threesquares(n: int):
    for a in range(n):
        for b in range(n):
            if n == pow(4, a) * (4 * b + 7):
                return False
    return True


# =============================================================================================


# Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once.
# The function should return True if there are no repetitions and False otherwise.

def repfree(s: str):
    check = [] # we make a empty list
    for i in s:
        if i in check: # we check that if that element already exists in the list if it exists then it return false
            return False
        else:
            check.append(i) # if the elemement is not present then we insert into the list
    return True


# A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence,
# where each of the sequences is of length at least two. Similarly, a list of numbers is said to be a valley hill if
# it consists of an descending sequence followed by an ascending sequence. You can assume that consecutive numbers in
# the input sequence are always different from each other.
#
# Write a Python function hillvalley(l) that takes a list l of integers and returns True
# if it is a hill or a valley, and False otherwise.

# =============================================================================================

def hillvalley(l: list):
    pos = -1
    if l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                pos = i
                break
        if pos == -1:
            return False
        for i in range(pos, len(l) - 1):
            if l[i] < l[i + 1]:
                return False
        return True
    elif l[0] > l[1]:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                pos = i
                break
        if pos == -1:
            return False
        for i in range(pos, len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    return False


# =============================================================================================


if __name__ == '__main__':
    # print(hillvalley([1, 2, 3, 5, 4]))
    # print(hillvalley([1, 2, 3, 4, 5]))
    # print(hillvalley([1, 2, 3, 4, 5, 3, 2, 4, 5, 3, 2, 1]))
    # print(repfree(input("Enter a string: ")))
    # print(threesquares(int(input("Enter a number: "))))
    # print(threesquares(int(input("Enter a number: "))))
    pass

def remdup(l: list):
    li: list = []
    for i in range(len(l)):
        if len(li) == 0:
            li.append(l[i])
        else:
            if l[i] in li:
                pass
            else:
                li.append(l[i])

    l = l = li
    return l


def sumsquare(l: list):
    odd = 0
    even = 0
    nl = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            even = even + l[i] ** 2
        else:
            odd = odd + l[i] ** 2
    nl.append(odd)
    nl.append(even)
    return f"[{odd}, {even}]"


def transpose(m: list):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez


if __name__ == '__main__':
    print(transpose([[1,2,3],[4,5,6]]))
    print(sumsquare([2, 4, 6]))
    print(remdup([3, 5, 7, 5, 3, 7, 10]))

"""
Week 4 Assignment
"""

"""
Define a Python function orangecap(d) that reads a dictionary d of this form
and identifies the player with the highest total score. Your function should return
a pair (playername,topscore) where playername is a string, the name of the player with
the highest score, and topscore is an integer, the total score of playername.
"""


def orangecap(d: dict):
    scoreList = {}
    largest = 0
    pos = ""
    for i in d:
        x = d[i]
        for j in x:
            if j in scoreList:
                check = scoreList[j]
                check = check + x[j]
                scoreList[j] = check
            else:
                scoreList[j] = x[j]
    for i, j in scoreList.items():
        if j > largest:
            pos = i
            largest = j
    return pos, largest


def addpoly(p1, p2):
    tree = {}
    z=[]
    for i in range(len(p1)):
        if p1[i][1] in tree:
            pass
        else:
            tree[p1[i][1]] = p1[i][0]
    for i in range(len(p2)):
        if p2[i][1] in tree:
            x = tree[p2[i][1]]
            tree[p2[i][1]] = x + p2[i][0]
            if tree[p2[i][1]] ==0:
                z.append(p2[i][1])
        else:
            tree[p2[i][1]] = p2[i][0]
    for i in z:
        del tree[i]
    ans=[]
    for i,j in tree.items():
        t=(j,i)
        ans.append(t)
    return sorted(ans)


def multpoly():
    pass


if __name__ == '__main__':
    check = orangecap({'match1': {'player1': 57, 'player2': 38}, 'match2': {'player3': 9, 'player1': 42},
                       'match3': {'player2': 41, 'player4': 63, 'player3': 91}})
    print(check)
    ans=addpoly([(4, 3), (3, 0)], [(-4, 3), (2, 1)])
    print(ans)

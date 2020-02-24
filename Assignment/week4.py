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


if __name__ == '__main__':
    check = orangecap({'match1': {'player1': 57, 'player2': 38}, 'match2': {'player3': 9, 'player1': 42},
                       'match3': {'player2': 41, 'player4': 63, 'player3': 91}})
    print(check)

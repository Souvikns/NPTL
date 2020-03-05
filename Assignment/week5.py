def takeInput():
    x = True
    ans = []
    while x:
        y = input()
        if y == "EndOfInput":
            return ans
        ans.append(y)
    return ans


def breakDate(s: str):
    x = s.split('-')
    return x


class Prog:
    def __init__(self):
        self.x = takeInput()
        self.books = {}
        self.borrowers = {}
        self.checkouts = {}
        self.counter = 0
        (self.b, self.bo, self.c) = (0, 0, 0)
        for i in self.x:
            if i == "Books":
                self.b = 1
            elif i == "Borrowers":
                self.bo = 1
            elif i == "Checkouts":
                self.c = 1
            if self.b == 1 and self.bo == 0 and self.c == 0:
                if i != "Books":
                    q = i.split('~')
                    self.books[q[0]] = q[1]
            elif self.b == 1 and self.bo == 1 and self.c == 0:
                if i != "Borrowers":
                    q = i.split('~')
                    self.borrowers[q[0]] = q[1]
            elif self.b == 1 and self.bo == 1 and self.c == 1:
                if i != "Checkouts":
                    self.checkouts[self.counter] = i.split('~')
                    self.counter = self.counter + 1

    def ans(self):
        q = []
        for i in self.checkouts:
            x = self.checkouts[i]
            q.append(f"{x[2]}~{self.borrowers[x[0]]}~{x[1]}~{self.books[x[1]]}")
        an = sorted(q)
        for i in an:
            print(i)


if __name__ == '__main__':
    # testprog()
    prog = Prog()
    prog.ans()

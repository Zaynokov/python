from random import randint


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mat = []
        for i in range(n):
            self.mat.append([randint(-20, 20) for k in range(m)])

    def __add__(self, other):
        for i in range(self.n):
            for k in range(self.m):
                self.mat[i][k] = self.mat[i][k] + other.mat[i][k]
        return Matrix.__str__(self)

    def __str__(self):
        self.res = ""
        for i in self.mat:
            h = str(i).replace("[", "")
            h = h.replace("]", "")
            h = h.replace(",", "  ")
            self.res += h + "\n"
        return self.res


a = Matrix(3, 3)
b = Matrix(3, 3)
print(a)
print(b)
print(a + b)

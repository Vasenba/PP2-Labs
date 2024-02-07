class myclass():
    def __init__(self,n,a):
        self.n = n
        self.a = a
    def __iter__(self):
        while self.a <= self.n:
            yield self.a * self.a
            self.a += 1
a = int(input())
n = int(input())

for t in myclass(n, a):
    print(t)

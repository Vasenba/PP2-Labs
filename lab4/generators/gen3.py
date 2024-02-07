class myclass:
    def __init__(self, n):
        self.n = n
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.a <= self.n:
            if self.a % 4 == 0 and self.a % 3 == 0:
                y = self.a
                self.a += 1
                return y
            else:
                self.a += 1
        raise StopIteration

n = int(input())
num = myclass(n)  
h = iter(num)  

for y in h: 
    print(y)


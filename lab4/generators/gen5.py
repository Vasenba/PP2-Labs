class gen():
    def __init__(self,n):
        self.n = n
        
    def __iter__(self):
        while self.n >= 0:
            yield self.n
            self.n -= 1


n = int(input())

for t in gen(n):
    print(t)

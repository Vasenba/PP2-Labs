class Mynum:
    def __init__(self, n):
        self.n = n
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= self.n:
            if self.a % 2 == 0:
                self.a += 1
                return self.a - 1
            else:
                self.a += 1
                return self.__next__()
        else:
            raise StopIteration

x = int(input())
b = []
num = Mynum(x)
for even_num in num:
    b.append(even_num)

print(b)

        
        
                

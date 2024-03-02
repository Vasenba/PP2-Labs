
a = str(input())
def poly(c):
    return c == c[::-1]
b = poly(a)
if(b == True):
    print("T")
elif(b == False):
    print("F")

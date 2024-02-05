def solve(numheads,numlegs):
    r = numlegs/2 - numheads
    return r
a = int(input("heads:"))
b = int(input("legs:"))

f = solve(a,b)
g = a - f
print("rabbit:",f,"""
chickens:""",g)

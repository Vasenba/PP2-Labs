n = int(input())
tl = list()
for i in range(n+1):
    if(i%2 == 0):
        tl.append(i)
    else:
        continue
tl.remove(0)    
print(tl)    

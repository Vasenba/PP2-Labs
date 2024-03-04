tlist = []
while True:
    x = input()
    if x == "":
        break
    tlist.append(x)
    
f = open("text1234","w")
for i in tlist:
    f.write(str(i))
    f.write("\n")
f.close()

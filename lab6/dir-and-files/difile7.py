f = open("text12.txt", "r")
a = open("text1.txt", "w")

for i in f:
    a.write(i)
    a.flush()
    
f.close()
a.close()

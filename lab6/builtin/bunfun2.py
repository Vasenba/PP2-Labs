t = str(input())

def ac(a,cnt):
    global t
    for i in range(0,len(t),1):
        if(ord(t[i])<90):
            cnt = cnt + 1
        else:
            continue
    return cnt
def acc(a,cny):
    global t
    for i in range(0,len(t),1):
        if(ord(t[i])>90):
            cny = cny + 1
        else:
            continue
    return cny
b = ac(1,0)
d = acc(1,0)

print(f"The big letter {b} , small ones {d}")

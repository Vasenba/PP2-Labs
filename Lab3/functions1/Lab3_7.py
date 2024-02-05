def has_33(nums):
    for i in range(0,len(nums),1):
        
        if(nums[i]==3):
                if(nums[i+1] == 3):
                    return True
        else:
            continue

thislist = []
x = 3
for i in range (x):
    a = int(input())
    thislist.append(a)

if(has_33(thislist)== True):
    print("True")
else:
    print("False")
          

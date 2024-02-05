def spy_game(nums):
    cntz = 0
    cnts = False
    for i in nums:
        if i == 0:
            cntz += 1
        elif i == 7 and cntz >= 2:
            cnts = True
            break
    return cnts


thelist = [int(x) for x in input("List: ").split()]

if spy_game(thelist):
    print("True")
else:
    print("False")

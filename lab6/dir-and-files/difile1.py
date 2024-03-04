import os
def dirandfiles(a):
    for b in os.listdir(a):
        if os.path.isdir(os.path.join(a, b)):
            print(b)
    for k in os.listdir(a):
        if os.path.isfile(os.path.join(a, k)):
            print(k)
    for files, dire, road in os.walk(a):
        for dir in dire:
            print(os.path.join(road, dir))
        for file in files:
            print(os.path.join(road, file))

dirandfiles(r"C:/Users/erasy/PP2/lab6/dir-and-files")


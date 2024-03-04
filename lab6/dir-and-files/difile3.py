import os
path = input("write path:")
def existf(path):
    if os.path.exists(path):  
        print("path exists")
        for dire, files, road in os.walk(path):
            if os.path.isdir(path):
                print("Dires:")
                print(os.path.join(dire, ""))

existf(path)

import shutil
import os
path=input("Enter dir path: ")
files=os.listdir(path)
print(files)
for i in files:
    name,ext=os.path.splitext(i)
    ext=ext[1:]
    if ext== "":
        continue
    if os.path.exists(path+"/"+ext):
        print(path+"/"+i)
        shutil.move(path+"/"+i,path+"/"+ext+"/"+i)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+i,path+"/"+ext+"/"+i)
import os
import shutil 

from_dir = "C:/Users/Shinj_28/Downloads"
list_of_files = os.listdir(from_dir)
to_dir="C:/Users/Shinj_28/OneDrive/Desktop/python" 

for filename in list_of_files:
    # Split the filename and extension
    name, extension = os.path.splitext(filename)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in ['.gif', '.html' , '.png' , '.ini' , '.jfif' , '.jpg']:
        path1= from_dir + '/' + filename
        path2= to_dir + '/' + "imagefiles"
        path3= to_dir + '/' + "imagefiles" + '/' + filename
        
        if os.path.exists(path2):
            print("moving" + filename + "..." )
            shutil.move (path1,path3)
        else :
            os.makedirs(path2)
            print("moving" + filename + "..." )
            shutil.move (path1,path3)
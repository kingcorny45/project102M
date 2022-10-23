import os
import shutil

from_dir = '/Users/cornelius/Desktop/Sans'
to_dir = '/Users/cornelius/Desktop/Papyrus'

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.jpeg','.png','.jpg','.gif','.jfif',".txt"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'TOP FUNNIEST JOKE EVER'
        path3 = to_dir + '/' + 'TOP FUNNIEST JOKE EVER' + '/' + file_name

        if os.path.exists(path2):
            print("moving all file!" + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving all file!" + file_name + "...")
            shutil.move(path1,path3)


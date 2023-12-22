import os
import shutil
from_dir='C102_assets-main'
to_dir='test'
list_of_files=os.listdir(from_dir)
for file in list_of_files:
    name, extension=os.path.splitext(file)
    if extension=='':
        continue
    if extension in ['.gif', '.png','.jpg','.jpeg','.jfif']:
        path1=from_dir+'/'+file
        path2=to_dir+'/'+"image_files"
        path3=to_dir+'/'+"image_files"+'/'+file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)

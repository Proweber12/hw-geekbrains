import os

subfolders =  ('settings','mainapp','adminapp','authapp')
for subfolder in subfolders:
   dir_path = os.path.join('my_project', subfolder)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)
import os,shutil
for folderName, subfolders, filenames in os.walk('M:\\MOVIES'):
    for filename in filenames:
        if os.path.getsize(f'{folderName}\\{filename}') > 4000000000:
            print('Files greater than 4000mb ' + folderName + ': '+ filename)
        else: continue
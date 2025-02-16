import os,shutil
for folderName, subfolders, filenames in os.walk('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter1'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        if filename.endswith('py'):
            print('FILE INSIDE ' + folderName + ': '+ filename)
            #print(f'{folderName}\\{filename}')
            #shutil.copy(f'{folderName}\\{filename}','I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\Ch1pyFiles')
        else: continue

    print()
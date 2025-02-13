import os,re, shutil
regex=re.compile(r'text$')
for folderName, subfolders, filenames in os.walk('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter1'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        if filename.endswith('py'):
            print('FILE INSIDE ' + folderName + ': '+ filename)
            #shutil.move(f'{folderName}{filename}','I:\\My Drive\\AutomateTheBoringStuffs\\Chapter1\\Ch1pyFiles')
        else: continue

    print('')
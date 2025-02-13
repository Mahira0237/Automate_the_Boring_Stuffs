# import send2trash
# baconFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\bacon.txt', 'a')   # creates the file
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash.send2trash('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\bacon.txt')

# import os

# for folderName, subfolders, filenames in os.walk('I:\\My Drive\\AutomateTheBoringStuffs'):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)

#     print('')

#"C:\\Users\\mahir\\Downloads\\abstract-blue-background.zip"
#c:\Users\mahir\Downloads\Backgrounds\107612-ONAIC3-767.jpg

# import zipfile, os
# from pathlib import Path
# p = Path.home()
# exampleZip = zipfile.ZipFile(p / "C:\\Users\\mahir\\Downloads\\abstract-blue-background.zip")
# exampleZip.extractall("C:\\Users\\mahir\\Downloads\\Backgrounds")

# exampleZip.extract('107612-ONAIC3-767.jpg')
# exampleZip.extract('107612-ONAIC3-767.jpg', 'C:\\Users\\mahir\\Downloads\\Backgrounds\\again')
# exampleZip.close()

#"C:\Users\mahir\Downloads\Backgrounds\License free.txt"
# import zipfile
# newZip = zipfile.ZipFile('C:\\Users\\mahir\\Downloads\\new.zip', 'w')   #'a' when you want to add files
# newZip.write('107612-ONAIC3-767.jpg', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()


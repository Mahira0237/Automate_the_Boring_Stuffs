import send2trash
baconFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\bacon.txt', 'a')   # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\bacon.txt')
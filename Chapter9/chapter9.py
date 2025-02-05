from pathlib import Path
import os

# helloFile = open('C:\\Users\\mahir\\hello.txt')
# helloContent = helloFile.read()
# print(helloContent)

#sonnetFile = open(Path.home() / 'sonnet29.txt')
#sonnetFile.readlines())

# baconFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\bacon.txt', 'w')   
# baconFile.write('Hello, world!\n')
# baconFile.close()
# baconFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# baconFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\bacon.txt')
# content = baconFile.read()
# baconFile.close()
# print(content)

import shelve
shelfFile = shelve.open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\mydata')
type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
print(cats)

import myCats
myCats.cats
print(myCats.cats[0])
print(myCats.cats[0]['name'])
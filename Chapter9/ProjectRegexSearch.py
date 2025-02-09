import os, glob,re
path = 'I:\\My Drive\\AutomateTheBoringStuffs\\Chapter9\\randomQuizGenerator'
regex=re.compile(input('Enter your regex: '))

for filename in glob.glob(os.path.join(path, '*.txt')):
      f=open(os.path.join(os.getcwd(), filename), 'r')
      print(regex.search(f.read()))
      f.close()
         
text = open('I:\My Drive\AutomateTheBoringStuffs\Chapter9\MadLibs.txt')
for content in text.readlines():
    while True:
        if 'ADJECTIVE' in content:
            content=content.replace('ADJECTIVE',input("Enter an adjective: "),1)
        if 'NOUN' in content:
            content=content.replace('NOUN',input("Enter a noun: "),1)
        if 'VERB' in content:
            content=content.replace('VERB',input("Enter a verb: "),1)
        else: break
    print(content,end='')

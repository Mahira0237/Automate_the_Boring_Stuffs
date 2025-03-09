import PyPDF2,sys
dictionary=open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter15\\dictionary.txt')
words=dictionary.readlines()
for i in range(0,len(words)):
    words[i]=words[i].replace('\n','')
    words.append(words[i].lower())
pdfFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter15\\encryptedminutes.pdf', 'rb')
for i in range(0,len(words)):
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.decrypt(words[i])==True:
        print("The password is "+words[i])
        sys.exit
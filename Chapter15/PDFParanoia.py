import os
import PyPDF2
for folderName, subfolders, filenames in os.walk('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter15\\PDFfilesToEncrypt'):
    print('The current folder is ' + folderName)

    for filename in filenames:
        if filename.endswith('.pdf'):
            print('The current file is ' + filename)
            pdfFile = open(f'{folderName}\\{filename}', 'rb')
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.encrypt(input("Enter a password: "))
            resultPdf = open(filename+'_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()            
            

#! python3
import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        #fullText.append('  ' + para.text)  FOR INDENTATION BEFORE EVERY PARAGRAPH
    return '\n'.join(fullText)
    #return '\n\n'.join(fullText) TO ADD DOUBLE SPACE 
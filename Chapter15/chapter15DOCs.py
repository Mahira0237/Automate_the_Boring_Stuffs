# # READING WORD DOCUMENTS
# import docx
# doc = docx.Document('demo.docx')
# print(len(doc.paragraphs))
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[1].text)
# print(len(doc.paragraphs[1].runs))
# print(doc.paragraphs[1].runs[0].text)
# print(doc.paragraphs[1].runs[1].text)
# print(doc.paragraphs[1].runs[2].text)
# print(doc.paragraphs[1].runs[3].text)
# print(doc.paragraphs[1].runs[4].text)

# import readDocx
# print(readDocx.getText('demo.docx'))

# # CHANGE DOC STYLE
# import docx
# doc = docx.Document('demo.docx')
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[0].style)
# doc.paragraphs[0].style = 'Normal'
# print(doc.paragraphs[1].text)
# print((doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
# paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text))
# doc.paragraphs[1].runs[0].style = 'Quote Char'
# doc.paragraphs[1].runs[1].underline = True
# doc.paragraphs[1].runs[3].underline = True
# doc.save('restyled.docx')

# # WRITING WORD DOCUMENTS
# import docx
# doc = docx.Document()
# doc.add_paragraph('Hello, world!')
# doc.save('helloworld.docx')

# import docx
# doc = docx.Document()
# doc.add_paragraph('Hello world!')
# paraObj1 = doc.add_paragraph('This is a second paragraph.')
# paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
# paraObj1.add_run(' This text is being added to the second paragraph.')
# doc.save('multipleParagraphs.docx')

# # ADDING HEADINGS
# import docx
# doc = docx.Document()
# doc.add_heading('Header 0', 0)
# doc.add_heading('Header 1', 1)
# doc.add_heading('Header 2', 2)
# doc.add_heading('Header 3', 3)
# doc.add_heading('Header 4', 4)
# doc.save('headings.docx')

# # ADDING LINE AND PAGE BREAKS
# import docx
# doc = docx.Document()
# doc.add_paragraph('This is on the first page!')
# doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
# doc.add_paragraph('This is on the second page!')
# # ADDING PICTURES
# doc.add_picture('perfume-bottle-nature.jpg', width=docx.shared.Inches(1),height=docx.shared.Cm(4))
# doc.save('twoPage.docx')


# import openpyxl
# import numpy as np
# wb = openpyxl.load_workbook('example.xlsx')
# print(type(wb))

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# print(wb.sheetnames)
# sheet = wb['Sheet3']
# print(sheet)
# print(type(sheet))
# print(sheet.title)
# anotherSheet = wb.active
# print(anotherSheet)

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb['Sheet1']
# print(sheet['A1'])
# print(sheet['A1'].value)
# c = sheet['B1']
# print(c.value)

# # Get the row, column, and value from the cell.

# print('Row %s, Column %s is %s' % (c.row, c.column, c.value))
# print('Cell %s is %s' % (c.coordinate, c.value))
# print(sheet['C1'].value)
# print(sheet.cell(row=1, column=2))
# print(sheet.cell(row=1, column=2).value)
# for i in range(1, 8, 2): # Go through every other row:
#     print(i, sheet.cell(row=i, column=2).value)

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet=wb['Sheet1']
# print(sheet.max_row)
# print(sheet.max_column)

# import openpyxl
# from openpyxl.utils import get_column_letter, column_index_from_string
# print(get_column_letter(1))
# print(get_column_letter(2))
# print(get_column_letter(27))
# print(get_column_letter(900))
# wb = openpyxl.load_workbook('example.xlsx')
# sheet=wb['Sheet1']
# print(get_column_letter(sheet.max_column))
# print(column_index_from_string('A'))
# print(column_index_from_string('AA'))

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet=wb['Sheet1']
# print(tuple(sheet['A1':'C3']))
# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet=wb.active
# print(list(sheet.columns)[1])
# for cellobj in list(sheet.columns)[1]:
#     print(cellobj.value)

# import openpyxl
# wb = openpyxl.Workbook()
# print(wb.sheetnames)
# sheet=wb.active
# print(sheet.title)
# sheet.title='Spam Bacon Eggs Sheet'
# print(wb.sheetnames)

# import openpyxl
# wb = openpyxl.load_workbook('example.xlsx')
# sheet = wb.active
# sheet.title = 'Spam Spam Spam'
# wb.save('example_copy.xlsx')

# # CREATE AND REMOVE SHEETS
# import openpyxl
# wb = openpyxl.Workbook()
# print(wb.sheetnames)
# print(wb.create_sheet())
# print(wb.sheetnames)
# # Create a new sheet at index 0.
# print(wb.create_sheet(index=0, title='First Sheet'))
# print(wb.sheetnames)
# print(wb.create_sheet(index=2, title='Middle Sheet'))
# print(wb.sheetnames)
# del wb['Middle Sheet']
# del wb['Sheet1']
# print(wb.sheetnames)

# # WRITING VALUES TO CELLS
# import openpyxl
# wb = openpyxl.Workbook()
# sheet= wb['Sheet']
# sheet['A1']='Hello, world!'
# print(sheet['A1'].value)

# # SETTING THE FONT STYLE OF CELLS
# import openpyxl
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']
# italic24Font = Font(size=24, italic=True) # Create a font.
# sheet['A1'].font = italic24Font # Apply the font to A1.
# sheet['A1'] = 'Hello, world!'
# wb.save('styles.xlsx')

# FONT OBJECTS
# import openpyxl
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']

# fontObj1 = Font(name='Times New Roman', bold=True)
# sheet['A1'].font = fontObj1
# sheet['A1'] = 'Bold Times New Roman'

# fontObj2 = Font(size=24, italic=True)
# sheet['B3'].font = fontObj2
# sheet['B3'] = '24 pt Italic'

# wb.save('styles.xlsx')

# # FORMULAS
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 200
# sheet['A2'] = 300
# sheet['A3'] = '=SUM(A1:A2)' # Set the formula.
# wb.save('writeFormula.xlsx')

# # SETTING ROW HEIGHT AND COLUMN WIDTH
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 'Tall row'
# sheet['B2'] = 'Wide column'
# # Set the height and width:
# sheet.row_dimensions[1].height = 70
# sheet.column_dimensions['B'].width = 20
# wb.save('dimensions.xlsx')

# MERGING AND UNMERGING CELLS
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.merge_cells('A1:D3') # Merge all these cells.
# sheet['A1'] = 'Twelve cells merged together.'
# sheet.merge_cells('C5:D5') # Merge these two cells.
# sheet['C5'] = 'Two merged cells.'
# wb.save('merged.xlsx')

# import openpyxl
# wb = openpyxl.load_workbook('merged.xlsx')
# sheet = wb.active
# sheet.unmerge_cells('A1:D3') # Split these cells up.
# sheet.unmerge_cells('C5:D5')
# wb.save('merged.xlsx')

# # FREEZING PANES
# import openpyxl
# wb = openpyxl.load_workbook('produceSales.xlsx')
# sheet = wb.active
# sheet.freeze_panes = 'A2' # Freeze the rows above A2.
# wb.save('freezeExample.xlsx')

# # CHARTS
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# for i in range(1, 11): # create some data in column A
#      sheet['A' + str(i)] = i
# refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
# seriesObj = openpyxl.chart.Series(refObj, title='First series')

# #chartObj = openpyxl.chart.LineChart()
# #chartObj = openpyxl.chart.ScatterChart()
# chartObj = openpyxl.chart.PieChart()
# #chartObj = openpyxl.chart.BarChart()
# chartObj.title = 'My Chart'
# chartObj.append(seriesObj)

# sheet.add_chart(chartObj, 'C5')
# wb.save('sampleChart.xlsx')
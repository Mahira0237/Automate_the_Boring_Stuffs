import os, openpyxl, csv 

for excelFile in os.listdir('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter16\\excelSpreadsheets'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    wb=openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:     
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]
        # # Create the CSV filename from the Excel filename and sheet title.
        csvFile = open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter16\\convertedToCSV'+'\\'+excelFile.replace('.xlsx','') + '_'+ sheetName, 'w', newline='\n')
        # # Create the csv.writer object for this CSV file.
        csvFileWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum,column=colNum).value)
            # Write the rowData list to the CSV file.
            csvFileWriter.writerow(rowData)
            
        csvFile.close()
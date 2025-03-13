# # READING OBJECTS
# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# #print(exampleData)

# print(exampleData[0][0])
# print(exampleData[0][1])
# print(exampleData[0][2])
# print(exampleData[1][1])
# print(exampleData[6][1])

# # READING DATA IN LOOP
# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#         print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# # WRITER OBJECTS
# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow([1, 2, 3.141592, 4]))
# outputFile.close()

# # The delimiter and lineterminator Keyword Arguments
# import csv
# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

# DictReader and DictWriter CSV Objects
# import csv
# exampleFile = open('exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)
# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])

# import csv
# exampleFile = open('example.csv')
# exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
# for row in exampleDictReader:
#     print(row['time'], row['name'], row['amount'])

# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
# outputDictWriter.writeheader()
# print(outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'}))
# print(outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'}))
# print(outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'}))
# outputFile.close()

# # Reading JSON with the loads() Function
# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# import json
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

# Writing JSON with the dumps() Function
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)




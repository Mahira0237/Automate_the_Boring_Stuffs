tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(tableData):
    max = 0
    for i in tableData:
        for j in i:
            if len(j) > max:
                max=len(j)
    j=0
    while j<(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(max),end='')
        print()
        j+=1

printTable(tableData)
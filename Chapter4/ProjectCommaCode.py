import sys
def takeList(theList):
    if theList==[]:
        print('The List can not be empty')
        sys.exit()
    theList.insert(-1,'and')
    for i in range(0,len(theList)-2):
        print(theList[i],end=', ')
    print(theList[-2] + ' ' + theList[-1])    

#spam= ['apples', 'bananas', 'tofu', 'cats']
spam=[]
takeList(spam)
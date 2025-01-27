import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    result=[]
    for i in range(100):
        flips = random.randint(0,1)
        if flips==0:
            result.append('H')
        else:
            result.append('T')
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(5,len(result)):
        #if result[j-5:j+1]== ('H H H H H H'.split() or 'T T T T T T'.split()):
        if result[j-5:j+1]== ((['H']*6) or (['T']*6)):
            numberOfStreaks+=1

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
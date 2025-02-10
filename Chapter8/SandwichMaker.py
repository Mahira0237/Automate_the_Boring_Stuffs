import pyinputplus as pyip

price=0
print('Lets make a sandwich for you.')
bread=pyip.inputMenu(['wheat','white','sourdough'],numbered=True,prompt='What type of bread would you like?\n')
if bread=='wheat': price+=20
elif bread=='white': price+=30
else: price+=40

protein=pyip.inputMenu(['chicken','turkey','ham','tofu'],numbered=True,prompt='\nWhich type of protein do you prefer?\n')
if protein=='chicken': price+=60
elif protein=='turkey': price+=80
elif protein=='ham': price+=100
else: price+=70

wantCheese=pyip.inputYesNo(prompt='\nDo you want cheese?\n',yesVal='yes'or'y'or'Y'or'Yes',noVal='no'or'n'or'N'or'No')
if wantCheese=='yes':
    cheese=pyip.inputMenu(['chedder','swiss','mozarella'],numbered=True,prompt='These are the available options.\n')
    if cheese=='chedder': price+=30
    elif cheese=='swiss': price+=40
    else: price+=50

wantmore=pyip.inputYesNo(prompt='\nWould you like sauce or any toppings?\n',yesVal='yes'or'y'or'Y'or'Yes',noVal='no'or'n'or'N'or'No')
if wantmore=='yes':
    more=pyip.inputMenu(['mayo','mustard','lettuce','tomato'],numbered=True,prompt='Available options:\n')
    if more=='mayo' or more=='mustard': price+=20
    else: price+=10

howMany=pyip.inputInt(prompt='\nHow many sandwitches do you want?\n',min=1)
print('\nTotal Cost is',price*howMany,'Tk')

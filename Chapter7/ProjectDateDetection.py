import re,sys

validation=re.compile(r'^([0-3][0-9])\/([0-1][0-9])\/([1-2][0-9]{3})')
check=validation.search('29/02/2000')
day=int(check.group(1))
month=int(check.group(2))
year=int((check.group(3)))

invalid='The Date is Invalid'
if month==2 and day==29 and year%400==0:
    print('It is leap year day')
    sys.exit
elif month==2 and day>=29 and year>999 and year<3000:
    print(invalid)
    sys.exit
elif (month==4 or month==6 or month==9 or month==11) and day==31 and year>999 and year<3000:
    print(invalid)
    sys.exit
else: print('The date is valid')
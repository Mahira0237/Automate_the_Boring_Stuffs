# import time
# time.time()

# READABLE TIME
# import time
# print(time.ctime())
# thisMoment = time.time()
# print(time.ctime(thisMoment))

# # SLEEP FUNCTION
# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)
# time.sleep(5)

# # ROUND FUNCTION
# import time
# now = time.time()
# print(now)
# print(round(now, 2))
# print(round(now, 4))
# print(round(now))

# # DATETIME MODULE
# import datetime
# print(datetime.datetime.now())
# dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)

#import datetime, time
# print(datetime.datetime.fromtimestamp(1000000))
# print(datetime.datetime.fromtimestamp(time.time()))

# halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# print(halloween2019 == oct31_2019)
# print(halloween2019 > newyears2020)
# print(newyears2020 > halloween2019)
# print(newyears2020 != oct31_2019)

# TIMEDELTA DATA TYPE
#import datetime
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

# dt = datetime.datetime.now()
# print(dt)
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)
# print(oct21st - aboutThirtyYears)
# print(oct21st - (2 * aboutThirtyYears))

# # Pausing Until a Specific Date
# import datetime
# import time
# halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

# # Converting datetime Objects into Strings
# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime("%B of '%y"))

# # Converting Strings into datetime Objects
# print(datetime.datetime.strptime('October 21, 2019', '%B %d %Y'))
# print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '19", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))

# # Passing Arguments to the Thread’s Target Function
# import threading
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# threadObj.start()

# import subprocess
# print(subprocess.Popen('C:\\Windows\\System32\\calc.exe'))

#import subprocess
# paintProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# print(paintProc.poll() == None)
# print(paintProc.wait()) # Doesn't return until MS Paint closes.
# print(paintProc.poll())

#subprocess.Popen(['C:\\Windows\\notepad.exe', 'I:\\My Drive\\AutomateTheBoringStuffs\\Chapter17\\hello.txt'])
#subprocess.Popen(['C:Users\\mahir\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe','I:\\My Drive\\AutomateTheBoringStuffs\\Chapter1\\hello.py'])

# fileObj = open('hello.txt', 'w')
# fileObj.write('Hello, world!')
# fileObj.close()
# import subprocess
# subprocess.Popen(['start', 'hello.txt'], shell=True)

import datetime
date = datetime.datetime(2019, 1, 7)
print(date.strftime("%A"))

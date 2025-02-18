#raise Exception('This is the error message.')

# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

# import logging
# logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')
# logging.critical('Critical error! Critical error!')
# logging.disable(logging.CRITICAL)
# logging.critical('Critical error! Critical error!')
# logging.error('Error! Error!')

# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# spam=int(input('Enter a number greater than or equal to 10: '))
# assert spam>10 or spam==10

# eggs='BoodBye'
# bacon='goodbye'
# assert eggs.lower()!=bacon.lower()

# assert 5==4


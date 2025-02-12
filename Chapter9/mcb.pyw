#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, time
mcbShelf = shelve.open('mcb')
# Save clipboard content. It is an Apple.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('Saved clipboard to',sys.argv[2])
    time.sleep(2)
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    print('Deleted key:',sys.argv[2]) 
    time.sleep(2)
elif len(sys.argv) == 2: 
    # List keywords and load content.
    if sys.argv[1].lower() == 'list': 
        pyperclip.copy(list(mcbShelf.keys())) 
        print('Listed all the keys') 
        time.sleep(2)
    if sys.argv[1].lower() == 'delete': 
        mcbShelf.clear()
        print('Deleted all the keys') 
        time.sleep(2)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('Text for ' + sys.argv[1] + ' copied to clipboard.')
        time.sleep(2)
mcbShelf.close() 
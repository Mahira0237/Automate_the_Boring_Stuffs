#! python3
# ProjectFillingInTheGaps.py - Rename text files with gaps also can insert gaps


import shutil, os, re

# Create a regex that matches files named with digits
filePattern = re.compile(r"""^(.*?) # all text before the digits
    (\d+)                     # digits at the end of text
     """, re.VERBOSE)        

for file in os.listdir('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\NumberedTextFiles'):
    if file.endswith('txt'):
        go=filePattern.search(file)

        if go==None:
            continue
        
        before=go.group(1)
        digits=go.group(2)

            

            
    
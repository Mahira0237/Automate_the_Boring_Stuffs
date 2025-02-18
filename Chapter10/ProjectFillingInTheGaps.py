#! python3
# ProjectFillingInTheGaps.py - Rename text files with gaps also can insert gaps


import shutil, os, re

# Create a regex that matches files named with digits
filePattern = re.compile(r"""^(.*?) # all text before the digits
    (0+)                     # digits at the end of text
    (\d+)                     # digits at the end of text
     """, re.VERBOSE)        
digits=[]
for file in os.listdir('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\NumberedTextFiles'):
    if file.endswith('txt'):
        go=filePattern.search(file)

        if go==None:
            continue

        before=go.group(1)
        zeros=go.group(2)
        digit=go.group(3)
        digits.append(int(digit))
        digits.sort()

    for i in range(digits[0],(int(digits[-1])+1)):
        if i not in digits:
            print(i)
            missing=i

            Working = 'I:\\My Drive\\AutomateTheBoringStuffs\\Chapter10\\NumberedTextFiles'
            prevFilename = f'{Working}\\{before}{zeros}{i+1}.txt'
            if int(digit) >9:               
                newFilename = f'{Working}\\{before}{zeros}{0}{i}.txt'
            else:
                newFilename = f'{Working}\\{before}{zeros}{i}.txt'
            print(f'Renaming "{prevFilename}" to "{newFilename}"...')
            #shutil.move(prevFilename, newFilename)   # uncomment after testing









            

            
    
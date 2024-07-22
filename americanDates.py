import re, os, shutil

# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYY


datePattern = re.compile(r"""^(.*?)    #all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)


# Loop over the files in the working directory.

for americanFile in os.listdir('-'):
    mo = datePattern.search(americanFile)

    #skip files that don't match
    if mo == None:
        continue

    #get the different parts of the file with regex groups 
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    yearPart = mo.group(4)
    dayPart = mo.group(6)
    afterPart = mo.group(8) 

    #now let's europise the files
    europFile = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #get the absoulte file path 
    absWorkingDir = os.path.abspath('.')
    americanFile =  os.path.join(absWorkingDir, americanFile)
    europFile = os.path.join(absWorkingDir, europFile)

    #rename files
    print(f'renaming "{americanFile}" to "{europFile}"...')
    shutil.move(americanFile, europFile)









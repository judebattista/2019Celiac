# Requirements:
# infileName: the name of the file to be parsed. Requires a directory prefix if you are running
#   the script from a directory other than that of the target file
#   default: lots.mol2
# delimiter: The line that separates atoms from each other
#   Unless the mol2 format changes, leave this alone
#   default: @<TRIPOS>MOLECULE
# outdirName: the directory you want the output files to be dumped into. Recommend keeping them
#   in a separate location to avoid shitting up your working directory
#   default: ./parsedMolFiles/
#   The default is a subdirectory of your script execution directory called parsedMolFiles
#   The script does not create the directory, so make sure it exists prior to execution
#   Note the trailing slash on the directory name!

# Feel free to comment out the print statements, they are for debugging and progress notifications

import re
infileName = 'lots.mol2'
delimiter = '@<TRIPOS>MOLECULE'
firstItem = True
outDirName = './parsedMolFiles/'

with open('lots.mol2', 'r') as infile:
    lines = []
    outfileName = ''
    # read contents line by line
    for line in infile:
        line = line.strip()
        # check to see if we've found the name
        if line[0:4] == 'ZINC':
            outfileName = dirName + line + '.mol2'
        # when we hit delimiter write list to file based on id
        if line == delimiter:
            print('Found the delimiter')
            # we need this check so we don't write a blank first file
            # not elegant, but this is a one time run
            # If we ever use this for larger scale projects, fix this
            if not firstItem:
                print('Writing lines to file {0}'.format(outfileName))
                # write lines to file
                with open (outfileName, 'w') as outfile:
                    for item in lines:
                        outfile.write(item + '\n')
                #reset the collection of lines for the next file
                lines = []
            else:
                firstItem = False
                print('firstItem was True, now switched to {0}'.format(firstItem))
        lines.append(line)
        print('lines has {0} items'.format(len(lines)))



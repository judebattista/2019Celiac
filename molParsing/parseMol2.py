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

infileName = 'fda.mol2'
delimiter = '@<TRIPOS>MOLECULE'
firstItem = True
outDirName = './parsedMolFiles/'
outfileFormat = '.mol2'

# Create the output file
# Note that it assumes the second line of the file is the molecule name,
#   which we use to name the output file
# We index the outfileName to account for multiple conformations of the same chemical structure
def printLinesToFile(lines, fileCountDict):
    outfileName = outDirName + lines[1]
    if outfileName in fileCountDict:
        fileCountDict[outfileName] += 1
    else:
        fileCountDict[outfileName] = 1
    outfileName = outfileName + '-' + str(fileCountDict[outfileName]) + outfileFormat
    with open (outfileName, 'w') as outfile:
        for item in lines:
            outfile.write(item + '\n')
    return fileCountDict

def run():
    outfileDict = {}
    lines = []
    outfileName = ''
    molName = ''
    firstItem = True
    #delimCount = 0
    #firstItemCount = 0
    with open(infileName, 'r') as infile:
        # read contents line by line
        for line in infile:
            line = line.strip()
            # when we hit delimiter write list to file based on id
            if line == delimiter:
                print('Found the delimiter')
                # we need this check so we don't write a blank first file
                # not elegant, but this is a one time run
                # If we ever use this for larger scale projects, fix this
                if not firstItem:
                    print('Writing lines to file {0}'.format(outfileName))
                    # write lines to file
                    outfileDict = printLinesToFile(lines, outfileDict)
                    #delimCount += 1
                    #reset the collection of lines for the next file
                    lines = []
                else:
                    firstItem = False
                    #firstItemCount += 1
                    print('firstItem was True, now switched to {0}'.format(firstItem))
            lines.append(line)
            print('lines has {0} items'.format(len(lines)))

        # Print the last set of lines
        outfileDict = printLinesToFile(lines, outfileDict)
        #print('Delimiters found: {0}, first items found: {1}'.format(delimCount, firstItemCount))

run()

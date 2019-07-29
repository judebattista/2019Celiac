filenames = 'fileNames'
molnames = 'moleculeNames'

files = []
mols = []

def printAnamoly(pair):
    sep = '+'*80
    print(sep)
    print()
    print(pair)
    print()
    print(sep)

with open(filenames, 'r') as infile:
    for name in infile:
        name = name.strip().split()[8][:-7]
        files.append(name)
    print('Found {0} file names.'.format(len(files)))

with open(molnames, 'r') as infile:
    for name in infile:
        name = name.strip()
        mols.append(name)
    print('Found {0} molecule names.'.format(len(mols)))

pairs = zip(files, mols)

mismatches = 0
for pair in pairs:
    if pair[0] != pair[1]:
        mismatches += 1
        printAnamoly(pair)

print('Found {0} mismatches.'.format(mismatches))


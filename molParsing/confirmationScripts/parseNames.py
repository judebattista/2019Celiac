infileName = 'fda.mol2'
outfileName = 'moleculeNames'
storeLine = False
delimiter = '@<TRIPOS>MOLECULE'

lines = []
with open(infileName, 'r') as infile:
    for line in infile:
        line = line.strip()
        if storeLine:
            lines.append(line)
            storeLine = False
        if line == delimiter:
            storeLine = True

lines = sorted(lines)

with open(outfileName, 'w') as outfile:
    for line in lines:
        outfile.write(line + '\n')
        

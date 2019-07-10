import csv

with open('idTest.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = True
    headerRow = []
    idHeader = 'id'
    idNdx = -1
    valid = True
    newFile = []
    for row in reader:
        if header:
            for ndx, element in enumerate(row):
                print('Row: {0}, index: {1}, element: {2}, checked against idHeader: {3}'.format(
                    row, ndx, element, idHeader 
                    ))
                if element == idHeader:
                    idNdx = ndx
            # If we did not find the id field
            if idNdx == -1:
                print("No id header found. Terminating")
                valid = False
            # If we did find the id field, we need to add a new column
            else:
                firstBit = row[0:idNdx+1]
                secondBit = row[idNdx+1:]
                headerRow.extend(firstBit)
                headerRow.append('cleanId')
                headerRow.extend(secondBit)
                print('header row: {0}'.format(headerRow)) 
            header = False
        elif valid:
            fullId = row[idNdx]
            cleanId = fullId[2:]
            firstBit = row[0:idNdx+1]
            secondBit = row[idNdx+1:]
            print('Row = {0}, first bit should be {1}, second bit should be {2}'.format(
                row, row[0:1], row[1:]))
            print('fullId: {0}, cleanId: {1}, first bit: {2}, second bit: {3}'.format(
                fullId, cleanId, firstBit, secondBit
                ))
            newRow = []
            newRow.extend(firstBit)
            newRow.append(cleanId)
            newRow.extend(secondBit)
            print('newRow: {0}'.format(newRow))
            newFile.append(newRow) 

with open('idTestClean.csv', 'w') as outfile:
    writer = csv.writer(outfile, delimiter=",")
    writer.writerow(headerRow)
    for row in newFile:
        writer.writerow(row)

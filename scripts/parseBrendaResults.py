from utilities import appendToDict, printDict

raw = []
kvpDict = {}
with open('results.raw', 'r') as infile:
    for line in infile:
       raw.append(line.strip())

testLine = raw[0]
splitLine = testLine.split('#')
#print('testline: {0}'.format(testLine))
#print('splitLine: {0}'.format(splitLine))
for pair in splitLine:
    kvp = pair.split('*')
    #print(kvp)
    if len(kvp) == 2:
        appendToDict(kvpDict, kvp[0], kvp[1])

printDict(kvpDict)

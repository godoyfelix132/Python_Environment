import fileinput

textToSearch = 'VDS_var'
textToReplace = 'word'

fileToSearch = root = 'C:\\Users\\Felix\\Desktop\\instrucciones.txt'

tempFile = open(fileToSearch, 'r+')

for line in fileinput.input(fileToSearch):
    tempFile.write(line.replace(textToSearch, textToReplace))
tempFile.close()

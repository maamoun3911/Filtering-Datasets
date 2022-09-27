import pandas as pd

csv_File_Address = './data/harrypotter_dataset.txt'

# Two helper function for findTitlesRows(csv_File_Address)
def getNextIndex(line, index):
    i = 0
    for word in line:
        if word[-3:] == "\"\"\"":
            return index + i
        else:
            i += 1
def poppingList(laLista, firstIndex, nextIndex): # line, wordIndex, lastIndex
    poppedList = [i for i in range(nextIndex, firstIndex, -1)]
    for number in poppedList:
        laLista.pop(number)
    return laLista

def findTitlesRows(csv_File_Address):
    with open (csv_File_Address, 'r') as txtFile:
        titleRow, rowsList = txtFile.readline().split(","), []
        for i in range(8):
            line, wordIndex = txtFile.readline().split(","), 0
            while wordIndex < len(line):
                word = line[wordIndex]
                if word[:4] == " \"\"\"":
                    lastIndex = getNextIndex(line[wordIndex:], wordIndex)
                    line[wordIndex] = line[wordIndex:lastIndex+1]
                    line = poppingList(line, wordIndex, lastIndex)
                wordIndex += 1
            rowsList.append(line)
    return titleRow, rowsList

# Making dictionary and fill with values
def makingDict(titleRow):
    dfDict= {}
    for title in titleRow:
        dfDict[title] = []
    return dfDict
def fillingDictWithValues(rowsList, dfDict):
    for row in rowsList:
        i = 0
        for key in dfDict.keys():
            if key == ' Director':
                dfDict[' Director'].append("Chris Columbs")
            else:
                dfDict[key].append(row[i])
                i += 1
    return dfDict

# main function
def main_func(csv_File_Address):
    titleRow, rowsList = findTitlesRows(csv_File_Address)
    dfDict = makingDict(titleRow)
    dfDict = fillingDictWithValues(rowsList, dfDict)
    HPDataFrame = pd.DataFrame(dfDict)
    return HPDataFrame

HPDataFrame = main_func(csv_File_Address)

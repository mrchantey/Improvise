from pkg.utilities import utility, itemUtils


def LoadMonologs(path):
    monologItem = utility.OpenJson('pkg/data/monologues.json')
    itemUtils.DoRecursive(monologItem, BreakoutText)
    return monologItem


def BreakoutText(item):
    if item['type'] != 'speech':
        return
    splitText = SplitAndReplaceMany(item['text'], ['.', '!', '?'])
    # splitText = SplitAndReplace(action['text'], '.')
    whiteRemoved = RemoveWhiteSpaceAtBeginning(splitText)
    item['text'] = whiteRemoved


def SplitAndReplaceMany(rawWord, delimeters):
    newArr = [rawWord]
    for delimeter in delimeters:
        nextArr = []
        for word in newArr:
            nextArr += SplitAndReplace(word, delimeter)
        newArr = nextArr
    return newArr


def SplitAndReplace(word, delimeter):
    splitWord = word.split(delimeter)
    # if splitWord[len(splitWord-1)] == '':
    # splitWord = splitWord[:-1]
    semiCombined = map(lambda w: w + delimeter, splitWord[:-1])
    semiCombined.append(splitWord[len(splitWord)-1])
    return semiCombined


def RemoveWhiteSpaceAtBeginning(wordArr):
    newArr = []
    for word in wordArr:
        # print "WORD>>" + word + "<<"
        if len(word) == 0:
            continue
        while word[0] == ' ':
            word = word[1:]
        newArr.append(word)
        # print "WORD>>" + word + "<<"
    return newArr

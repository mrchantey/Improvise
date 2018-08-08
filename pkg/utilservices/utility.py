import json


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def OpenJson(path):
    file = open(path, 'r')
    txt = file.read()
    uniJsn = json.loads(txt)
    pyJsn = parseType(uniJsn)
    # print uniJsn
    # print pyJsn
    file.close()
    return pyJsn


def OpenTextLines(path):
    file = open(path, 'r')
    text = file.read()
    text.replace('\r', '')  # remove dos line endings
    lines = text.split('\n')
    return lines


def parseType(val):
    if isinstance(val, unicode):
        newVal = val.encode('ascii', 'ignore')
        if isInt(newVal):
            return int(newVal)
        return newVal
    elif isinstance(val, str):
        if isInt(val):
            return int(val)
        return val
    elif isinstance(val, dict):
        return parseUnicodeDict(val)
    elif isinstance(val, list):
        return parseUnicodeList(val)
    elif isinstance(val, int) or isinstance(val, str) or isinstance(val, bool) or isinstance(val, float):
        return val
    elif val == None:
        return val
    print '\n\n unknown type', '\n', type(val), '\n', val
    return val


def parseUnicodeDict(dict):
    res = {}
    for key, value in dict.iteritems():
        key = parseType(key)
        res[key] = parseType(value)
    return res


def parseUnicodeList(lst):
    res = []
    for item in lst:
        res.append(parseType(item))
    return res


# 'r' = read, 'w' = write, 'a' = append, 'r+' = read and write

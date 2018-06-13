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
    pyJsn = parseUnicode(uniJsn)
    # print uniJsn
    # print pyJsn
    file.close()
    return pyJsn


def parseUnicode(val):
    if isinstance(val, unicode):
        newVal = val.encode('ascii', 'replace')
        if isInt(newVal):
            return int(newVal)
        else:
            return newVal
    elif isinstance(val, dict):
        return parseUnicodeDict(val)
    elif isinstance(val, list):
        return parseUnicodeList(val)
    elif isinstance(val, int):
        return val
    elif isinstance(val, str):
        return val
    elif isinstance(val, bool):
        return val
    elif val == None:
        return val
    print '\n\n unknown type', type(val)
    return val


def parseUnicodeDict(dict):
    res = {}
    for key, value in dict.iteritems():
        key = parseUnicode(key)
        res[key] = parseUnicode(value)
    return res


def parseUnicodeList(lst):
    res = []
    for item in lst:
        res.append(parseUnicode(item))
    return res

# 'r' = read, 'w' = write, 'a' = append, 'r+' = read and write

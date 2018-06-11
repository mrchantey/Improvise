
def parseUnicode(val):
    if isinstance(val, unicode):
        newVal = val.encode('ascii', 'replace')
        if isInt(newVal):
            return int(newVal)
        else:
            return newVal

    else:
        return val


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

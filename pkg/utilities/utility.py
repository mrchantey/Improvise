import json
from xml.etree import ElementTree


def OpenJson(path):
    file = open(path, 'r')
    txt = file.read()
    file.close()
    uniJsn = json.loads(txt)
    pyJsn = parseType(uniJsn)
    # print uniJsn
    # print pyJsn
    return pyJsn


def ElementTreeToDict(tree):
    d = {tree.tag: map(ElementTreeToDict, tree.getchildren())}
    d.update(('@' + k, v) for k, v in tree.attrib.iteritems())
    d['xmlValue'] = tree.text
    return d


def OpenXml(path):
    # file = open(path, 'r')
    # txt = file.read()
    # file.close()
    tree = ElementTree.parse(path).getroot()
    rawObj = ElementTreeToDict(tree)
    pyObj = parseType(rawObj)
    return pyObj


def OpenTextLines(path):
    file = open(path, 'r')
    text = file.read()
    text.replace('\r', '')  # remove dos line endings
    lines = text.split('\n')
    return lines


def parseStringAsDict(valStr):
    # print "STRING VERSION", valStr
    valStrClean = (valStr
                   .decode('string-escape')
                   .strip('"')
                   # seems to cope with new line and escape characters just fine
                   #    .replace("\\n", "")
                   #    .replace("\\", "")
                   #    .replace("\\", "")
                   #    .replace("\n", "")
                   )
    # print "UESCAPED STRING VERSION", valStrClean
    valDict = json.loads(valStrClean)
    # print "JSON VERSION", valDict
    valDictClean = parseType(valDict)
    # print "CLEAN JSON VERSION", valDictClean
    return valDictClean


def parseDictAsString(valDict):
    return json.dumps(valDict)


def parseType(val):
    if isinstance(val, unicode):
        newVal = val.encode('ascii', 'ignore')
        return parseString(newVal)
    elif isinstance(val, str):
        return parseString(val)
    elif isinstance(val, dict):
        return parseUnicodeDict(val)
    elif isinstance(val, list):
        return parseUnicodeList(val)
    elif (val == None
            or isinstance(val, int)
            or isinstance(val, bool)
            or isinstance(val, float)):
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


def parseString(val):
    try:
        iVal = int(val)
        return iVal
    except ValueError:
        pass
    try:
        fVal = float(val)
        return fVal
    except ValueError:
        pass
    if val == 'true'or val == 'True':
        return True
    elif val == 'false' or val == 'False':
        return False
    else:
        return val


def GetMimeType(path):
    splitPath = path.split('.')
    lastIndex = len(splitPath)-1
    extension = splitPath[lastIndex]
    if extension == 'html':
        return 'text/html'
    elif extension == 'js':
        return 'text/javascript'
    elif extension == 'css':
        return 'text/css'
    elif extension == 'ico':
        return 'image/x-icon'
    else:
        print 'unknown extension', extension
        return 'text'
# 'r' = read, 'w' = write, 'a' = append, 'r+' = read and write


if __name__ == "__main__":
    # myStr = '"\"[\\n    {\\n        \\\"commandName\\\": \\\"action\\\",\\n        \\\"actionName\\\": \\\"Left Forearm Pronation / Supination\\\",\\n        \\\"triggerPhrase\\\": \\\"Left Forearm Pronation and Supination\\\",\\n        \\\"subCommands\\\": [\\n            {\\n                \\\"commandName\\\": \\\"loopAction\\\",\\n                \\\"loopCount\\\": 3,\\n                \\\"startCommands\\\": [\\n                    {\\n                        \\\"commandName\\\": \\\"runBehavior\\\",\\n                        \\\"path\\\": \\\"custom_animations/body/stand\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"say\\\",\\n                        \\\"phrase\\\": \\\"Lets do forearm pronation and supination. Start by raising your left elbow.\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"pose\\\",\\n                        \\\"async\\\": true,\\n                        \\\"poseName\\\": \\\"Head/look_down_left\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"pose\\\",\\n                        \\\"poseName\\\": \\\"LArm/elbow_fwd_90\\\"\\n                    }\\n                ],\\n                \\\"loopCommands\\\": [\\n                    {\\n                        \\\"commandName\\\": \\\"pose\\\",\\n                        \\\"poseName\\\": \\\"LWrist/forearm_pronation\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"internal\\\",\\n                        \\\"instruction\\\": \\\"pause\\\",\\n                        \\\"duration\\\": 1\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"pose\\\",\\n                        \\\"poseName\\\": \\\"LWrist/forearm_supination\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"internal\\\",\\n                        \\\"instruction\\\": \\\"pause\\\",\\n                        \\\"duration\\\": 1\\n                    }\\n                ],\\n                \\\"endCommands\\\": [\\n                    {\\n                        \\\"commandName\\\": \\\"pose\\\",\\n                        \\\"poseName\\\": \\\"Full/stand\\\"\\n                    },\\n                    {\\n                        \\\"commandName\\\": \\\"say\\\",\\n                        \\\"phrase\\\": \\\"Good job!\\\"\\n                    }\\n                ]\\n            }\\n        ]\\n    }\\n]\""'
    # parseStringAsDict(myStr)
    # obj = OpenXml('pkg/utilities/text.xml')
    obj = OpenXml('choregraphe/physio_pose_library.xap')
    print obj

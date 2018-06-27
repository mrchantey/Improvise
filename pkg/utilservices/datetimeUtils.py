import datetime
import dateutil.parser
# from datetime import date, time
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DIGIT0 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIGIT1 = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
DIGITN = ["", "hundred", "thousand", "hundred thousand", "million"]
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ORDINAL = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelvth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty first", "twenty second", "twenty third", "twenty fourth", "twenty fifth", "twenty sixth", "twenty seventh", "twenty eighth", "twenty ninth", "thirtieth", "thirty first"]


def GetNumberWord(number):
    if number == 0:
        return DIGIT0[0]
    word = ""
    mod100 = number % 100
    mod10 = number % 10

    for i in range(3, 1, -1):
        iPow = 10 ** i
        iPowMax = 10 ** (i + 1)
        iN = i - 1

        # print "{0} {1} {2} {3}".format(number, iPow, iPowMax, iN)
        iMod = number % iPowMax
        if iMod >= iPow:
            fract = iMod / iPow
            # print 'fract {0} / {1} digitn {2} / {3}'.format(fract, len(DIGIT0), iN, len(DIGITN))
            if word != "":
                word += ", "
            word += "{0} {1}".format(DIGIT0[fract], DIGITN[iN])
    if mod100 == 0:
        return word
    if word != "":
        word += " and "

    # if number >= 100:
    #     word += "{0} {1}".format(DIGIT0[number / 100], DIGITN[1])
    #     if mod100 != 0:
    #         word += " and "
    if mod100 > 9 and mod100 < 20:
        word += TEENS[mod100 % 10]
        return word
    elif mod100 >= 20:
        word += DIGIT1[int(mod100 / 10)]
    if mod10 != 0:
        word += DIGIT0[mod10]
    return word


def GetDayOfWeek(date):
    dow = date.isoweekday()
    return DAYS[dow]


def GetTimeWords(time):
    period = "a m" if time.hour < 12 else "p m"
    hournum = time.hour if time.hour <= 12 else time.hour-12
    if hournum == 0:
        hournum = 12
    hour = GetNumberWord(hournum)
    minute = GetNumberWord(time.minute)
    if minute == "zero":
        minute = "o clock"
    return "{0} {1} {2}".format(hour, minute, period)


def GetDateWords(date, includeYear=True):
    dayWeek = GetDayOfWeek(date)
    dayMonth = ORDINAL[date.day]
    month = MONTHS[date.month]
    phrase = "{0} the {1} of {2}".format(dayWeek, dayMonth, month)
    if not includeYear:
        return phrase
    return phrase + ", {0}".format(GetNumberWord(date.year))


def ParseDateFromString(stringDate):
    return dateutil.parser.parse(stringDate).date()


if __name__ == "__main__":
    dateTime = ParseDateFromString('2018-06-10T20:33:32Z')
    date = dateTime.date()
    print type(date)
    print GetDateWords(date)
    # print ParseDateFromString('2018-06-10T20:33:32Z')
    # for i in range(0, 1000):
    #     print GetNumberWord(i)
    # now = datetime.datetime.now().date()
    # print GetDateWords(now)

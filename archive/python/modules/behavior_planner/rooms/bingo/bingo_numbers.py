import random
import math
from pkg.utilities import utility


class BingoNumbers():
    def __init__(self, min, max, loop=False):
        self.calledNumbers = []
        self.loop = loop
        self.min = min
        self.max = max
        self.phrases = utility.OpenTextLines('pkg/data/bingo-calls.txt')
        self.Shuffle()

    def IsDone(self):
        return False if len(self.calledNumbers) > 0 else True

    def Shuffle(self):
        self.calledNumbers = []
        for i in range(self.min, self.max+1):
            self.calledNumbers.append(i)
        random.shuffle(self.calledNumbers)

    def GetNextBingoCall(self):
        num = self.GetNextNumber()
        if num == None:
            return None
        numberCall = 'number ' + str(num) + '...'
        call = numberCall
        if num < len(self.phrases):
            call += " " + self.phrases[num] + '...'
        if num > 9:
            call += " " + str(math.floor(num/10))[0]
            call += " " + str(num % 10) + '...'
        call += ' ' + numberCall
        return call

    def GetNextNumber(self):
        if len(self.calledNumbers) > 0:
            return self.calledNumbers.pop()
        elif self.loop:
            print 'bang'
            self.Shuffle()
            return self.GetNextNumber()

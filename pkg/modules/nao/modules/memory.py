

class MemoryModule():

    def __init__(self,memoryService):

        self.memory = memoryService
        
        customData = [
            ("physioDefaultRepetitions",2),
            ("physioOneShotRepetitions",-1)
        ]
        
        self.InitializeData(customData)

    def InitializeData(self,customData):
        for data in customData:
            self.InsertData(data[0],data[1])

    def InsertData(self,key,value):
        self.memory.insertData(key,value)

    def GetData(self,key):
        try:
            return self.memory.getData(key)
        except:
            return "key not found: " + key
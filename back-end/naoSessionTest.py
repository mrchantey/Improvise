from naoSession import NaoSession

testIP = '10.50.16.67'


session = NaoSession()

session.Connect(testIP)
session.Say('hello')

# def test():
#     beginSession(testIP)
#     print 'session connected'
#     tts = session.service("ALTextToSpeech")

#     def saySomething():
#         onSaid = tts.say('hi there... nice to meet you', _async=True)
#         val = onSaid.value()
#         print 'all done,  value = ', val
#     print '\n1'
#     runAsync(saySomething)
#     print '\n2'
#     runAsync(saySomething)
#     print '\n3'
#     runAsync(saySomething)

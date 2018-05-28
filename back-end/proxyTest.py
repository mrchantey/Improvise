from naoProxy import NaoProxy

nao = NaoProxy()

success = nao.Connect('10.50.16.67')

print 'success:', success

# WaitForDone(onSaid)
# onSaidNext = tts.say('hi there... nice to meet you', _async=True)
# tts = ALProxy('ALTextToSpeech', testIP, 9559)
# print 'begin speaking ', time.time()
# id = tts.post.say("hello, world!")
# print 'id is ', id
# print 'finished speaking ', time.time()

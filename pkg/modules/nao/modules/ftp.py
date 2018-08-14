from pkg.utilities.ftpClient import FTPClient
import time


class FTPModule(FTPClient):
    def __init__(self, address):
        FTPClient.__init__(self, address, 'nao', 'nao')

    def GetLastSentence(self):
        # print 'changing directory'
        # print self.ftp.pwd()
        # print self.ftp.retrlines('LIST')
        # self.ftp.cwd('/')
        # print self.ftp.pwd()
        # print self.ftp.retrlines('LIST')
        # self.ftp.cwd('custom/improvise')
        # print self.ftp.pwd()
        # print self.ftp.retrlines('LIST')
        self.Login()
        self.tempData = ''

        def appendData(val):
            self.tempData += val

        # self.ftp.retrbinary('RETR last_sentence.wav', appendData)
        self.ftp.retrbinary('RETR custom/improvise/last_sentence.wav', appendData)
        self.Logout()
        return self.tempData


if __name__ == "__main__":
    client = FTPModule('10.50.16.63')
    client.Login()
    time.sleep(10)
    data = client.GetLastSentence()
    print len(data)
    client.Logout()

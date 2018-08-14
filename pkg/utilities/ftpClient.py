from ftplib import FTP


# ftp = FTP('10.50.16.63')
# # ftp = FTP('speedtest.tele2.net')
# # ftp.login()
# ftp.login(user='nao', passwd='nao')


class FTPClient():
    def __init__(self, address, username, password):
        self.address = address
        self.ftp = FTP(address)
        self.username = username
        self.password = password

    def Login(self):
        self.ftp.login(user=self.username, passwd=self.password)
        print self.ftp.getwelcome()

    def Logout(self):
        self.ftp.close()

# multiple host simultaneous control.
import optparse
import pxssh
class Client:
    # constructor
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    #connect
    def connect(self):
        try:
            s = pxssh.pxss()
            s.login(self.host, self.user, self.password)
            s
        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        self.session.before

    def botnetCommand(command):
        for client in botNet:
            output = client.send_command(command)
            print '[*] Output from ' + client.host
            print '[+] ' + output + '\n'

    def addClient(host, user, password):
        client = Client(host, user, password)
        botNet.append(client)
    botNet []
    addClient('10.10.10.110','root', 'chicken')
    addClient('10.10.10.120','root', 'chicken')
    addClient('10.10.10.130','root', 'chicken')
    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')

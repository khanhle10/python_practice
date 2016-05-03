import pexcept
PROMPT = ['#', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey = 'Do you want to continue...'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    retr = pexpect([pexpect.TIMEOUT, ssh_newkey, \
    '[P|p]assword:'])
    if retr == 0:
        print '[-] Error Connecting'
        return
    if retr == 1:
        child.sendline('yes')
        retr = child.expect([pexpect.TIMEOUT, \
        '[P|p]assword:'])
        if retr == 0:
            print '[-] Error Connecting'
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'chicken'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow |grep root')

if __name__ == '__main__':

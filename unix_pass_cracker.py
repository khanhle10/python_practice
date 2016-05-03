import crypt

def testPass(cryptPass):
    salt_test = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word.salt_test)
        if (cryptWord == cryptPass):
             print '[+] Password Found: ' + word + '\n'
             return
    print '[-] Password Not Found.\n'
    return
def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print '[*] Cracking Password for: '+ user
            testPass(cryptPass)
if __name__ == '__main__':
    main()
    

# tcp scanner to identify host.
import optparse
import socket
import nmap
from socket import *
from threading import *
# threading scanning
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Connect With Python\r\n')
        result = connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open '% tgtPort
        pritn '[+] ' + str(result)
        connSkt.close()
    except:
        print '[-]%d/tcp closed' % tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print ' [*] ' + tgtHost + ' tcp/'+ tgtPort + ' ' + state

def portScan(tgtHost, tgtPort):
    try:
        tgtIP = getHostName(tgtHost)
    except:
        print '[-] Cannot resolve '%s': Unknown host' %tgtHost
        return
    try:
        tgtName = getHostAddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    setDefaultTimeOut(1)
    for port in tgtPort:
        print 'Scanning Port ' + port
        thr = Thread(target=connScan, args=(tgtHost, int(port)))
        thr.start()
def main():
    parser = optparse.OptionParser('usage%prog '+\
    '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',\
    help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',\
    help='specify target port separate by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(', ')
    if(tgtHost == None) | (tgtPort[0] == None):
        print '[-] Please specify the target host and port.'
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPort)
if __name__ == '__main__':
    main()

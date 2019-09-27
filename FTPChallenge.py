# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo URL: https://github.com/devonknudsen/FTP-Covert
# Written in Python 3.7

from ftplib import FTP

METHOD = 10
SERVER = '138.47.149.96'
PORT = 8008
USERNAME = 'spartans'
PASSWORD = 'spartansSPARTANSspartans'

# appends the file permissions to a list
def retrieveFilePerms():
    if(METHOD == 7):
        ftp.cwd('.lookee-here/now-in-here')
    if(METHOD == 10):
        ftp.cwd('.lookee-here/now-in-here')

    filePerms = []
    ftp.retrlines('LIST', filePerms.append)
    filePerms = [filePerms[i][:10] for i in range(len(filePerms))]

    ftp.quit()
    
    return filePerms

# removes the 'noise' from messages made of 7 right most bits
def removeNoise(pList):
    newList = []
    for pSet in pList:
        if(pSet[:3] == '---'):
            newList.append(pSet)

    return newList

# converts each index of file permissions into binary
def permsToBinaryList(pList):
    if(METHOD == 7):
        for i in range(len(pList)):
            pList[i] = pList[i] [3:]

    if(METHOD == 10):
        pList = ''.join(pList)
        pList = [pList[i:i + 7] for i in range(0, len(pList), 7)]

    for i in range(len(pList)):
        currPerm = pList[i]
        currPerm = currPerm.replace('-', '0')
        currPerm = currPerm.replace('d', '1')
        currPerm = currPerm.replace('w', '1')
        currPerm = currPerm.replace('r', '1')
        currPerm = currPerm.replace('x', '1')
        pList[i] = currPerm

    return pList

# decodes the binary into the plain text message
def binaryToText(pList):
    completeMessage = ''
    
    for i in range(len(pList)):
        asc = int(pList[i], 2)

        # if: there's a backspace
        if(asc == 8):
            completeMessage = completeMessage[:-1]
        else:
            newChar = chr(asc)
            completeMessage += newChar
    
    return completeMessage


# MAIN
#ftp = FTP(SERVER, PORT)

ftp = FTP()
ftp.connect(SERVER, PORT)
ftp.login(USERNAME, PASSWORD)

if(METHOD == 7):
    fPs = retrieveFilePerms()
    refinedfPs = removeNoise(fPs)
    binaryList = permsToBinaryList(refinedfPs)
    print(binaryToText(binaryList))
    message = binaryToText(binaryList)

if(METHOD == 10):
    fPs = retrieveFilePerms()
    binaryList = permsToBinaryList(fPs)
    print(binaryToText(binaryList))
    message = binaryToText(binaryList)
    
            


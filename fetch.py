# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo URL: https://github.com/devonknudsen/FTP-Covert
# Written in Python 3.7

from ftplib import FTP

METHOD = 7
serverURL = 'jeangourd.com'
username = 'anonymous'
password = ''

# appends the file permissions to a list
def retrieveFilePerms():
    filePerms = []
    ftp.retrlines('LIST', filePerms.append)
    filePerms = [filePerms[i][:10] for i in range(len(filePerms))]
    
    return filePerms

# removes the 'noise' from messages made of 7 right most bits
def removeNoise(pList):
    for pSet in pList:
        if(pSet[:3] != '---'):
            pList.remove(pSet)

# converts each index of file permissions into binary
def permsToBinaryList(pList):
    if(METHOD == 7):
        for pSet in pList:
            pSet = pSet[3:]

    for i in range(len(pList[i])):
        currPerm = pList[j]
        for j in range(len(currPerm)):
            if(currPerm[j] == '-'):
                currPerm[j] = '0'
            else:
                currPerm[j] = '1'

    return pList

# decodes the binary into the plain text message
def binaryToText(pList):
    completeMessage = ''
    
    for i in range(0, len(pList)):
        asc = int(pList[i], 2)

        # if: there's a backspace check
        if(asc == 8):
            completeMessage = completeMessage[:-1]
        else:
            newChar = chr(asc)
            completeMessage += newChar
    
    return completeMessage


# MAIN
ftp = FTP(serverURL)
ftp.login(username, password)

if(METHOD == 7):
    ftp.cwd('7')
    fPs = retrieveFilePerms()
    removeNoise(fPs)
    permsToBinaryList(fPs)
    print(binaryToText)


if(METHOD == 10):
    ftp.cwd('10')
    fPs = retrieveFilePerms()
    permsToBinaryList(fPs)
    print(binaryToText)

    
        
        



#!/usr/bin/python
import re
import subprocess
import sys

def follow(file):
    countHiwi = 0
    countUserLogin = 0
    countGroups = 0
    countFileSize = 0
    countEmailNumber = 0
    countWarnings = 0
    countErrors = 0

    userLoginPattern = re.compile(r'\b.*login.*\b | \b.*logged in.*\b  ', flags=re.I | re.X)
    groupsNumber = re.compile(r'\b.*group.*created\b  ', flags=re.I | re.X)
    fileUploadedSize = re.compile(r'\b.*file_uploaded\b  ', flags=re.I | re.X)
    libraryNumber = re.compile(r'\b.*library.*created\b  ', flags=re.I | re.X)
    emailSent = re.compile(r'\b.*send_notices:278.*Successfully sent email to\b  ', flags=re.I | re.X)
    warnings  = re.compile(r'\b.*Warning.*\b  ', flags=re.I | re.X)
    errors = re.compile(r'\b.*Error.*\b  ', flags=re.I | re.X)
    file.seek(0,2)
    while True:
        #flag = file.tell()
        line = file.readline()
        if not line:
            #file.seek(flag)
            continue
        if userLoginPattern.match(line):
            with open("userLogin.log","a+") as userLoginFile:
                countUserLogin += 1
                userLoginFile.write(line+"Counted: %d \n"%(countUserLogin))
                print line,
                continue 
        if groupsNumber.match(line):
            with open("NumberOfGroups.log","a+") as groupNumberFile:
                countGroups += 1
                groupNumberFile.write(line+"Counted: %d \n"%(countGroups))
                print line,
                continue
        if fileUploadedSize.match(line):
            with open("FileSize.log","a+") as fileSizeFile:
                countFileSize += 1
                fileSizeFile.write(line+"Counted: %d \n"%(countFileSize))
                print line,
                continue
        if libraryNumber.match(line):
            with open("NumberOfLibrary.log","a+") as libraryNumberFile:
                countLibraryNumber += 1
                fileSizeFile.write(line+"Counted: %d \n"%(countLibraryNumber))
                print line,
                continue
        if libraryNumber.match(line):
            with open("NumberOfEmails.log","a+") as emailsNumberFile:
                countEmailNumber += 1
                emailsNumberFile.write(line+"Counted: %d \n"%(countEmailNumber))
                print line,
                continue
        if warnings.match(line):
            with open("Warnings.log","a+") as warningsFile:
                countWarnings += 1
                warningsFile.write(line+"Counted: %d \n"%(countWarning_Found))
                print line,
                continue
        if errors.match(line):
            with open("Errors.log","a+") as errorsFile:
                countErrors += 1
                errorsFile.write(line+"Counted: %d \n"%(countWarning_Found))
                print line,
                continue
        else:
            print line,

if __name__ == '__main__':
    try:

        logfile = open("/data/syslog/seafile/seafile.rlp.net.log","r")
        logLines = follow(logfile)
    except IOError:
        print "Could not read file:", logfile
        sys.exit()

import sys
import glob
import errno
import re
import csv
import os
import multiprocessing
from subprocess import call

def firstCSV(quarterList, finalList):
    with open('ipblacklist01.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for y in range(0, quarterList):
            writer.writerow(finalList[y])
    print("\nGenerated first CSV file...\n")

def secondCSV(quarterList, halfList, finalList):
    with open('ipblacklist02.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for x in range(quarterList, halfList):
            writer.writerow(finalList[x])
    print("\nGenerated second CSV file...\n")

def thirdCSV(halfList, threeQuarterList, finalList):
    with open('ipblacklist03.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for x in range(halfList, threeQuarterList):
            writer.writerow(finalList[x])
    print("\nGenerated third CSV file....\n")

def fourthCSV(threeQuarterList, fullList, finalList):
    with open('ipblacklist04.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for x in range(threeQuarterList, fullList):
            writer.writerow(finalList[x])
    print("\nGenerated final CSV file\n")

if __name__ == "__main__":
    # Declarations
    x = 0
    iplist = []
    uniqueIpList = []
    finalList = []
    ipPattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    # Check if blocklist-ipsets repo is in the current folder, otherwise it will git clone it
    if not os.path.exists("blocklist-ipsets/"):
        print("\n Did not find blocklist-ipsets repo in current directory, will try to git clone it... \n")
        call(["git", "clone", "https://github.com/firehol/blocklist-ipsets.git"])
    path = "blocklist-ipsets/*.ipset"
    files = glob.glob(path)

    # Creating huge list of all blacklisted IPs
    for name in files:
        try:
            with open(name) as f:
                for line in f.readlines():
                    ipMatch = re.search(ipPattern, line)
                    if ipMatch:
                        iplist.append(str(name) + "," + line.replace('\n',''))
        except IOError as exc:
            if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                raise # Propagate other kinds of IOError.

    # Creating list of unique blacklisted IPs
    uniqueIpList = list(set(iplist))
    for ip in uniqueIpList:
        finalList.append(ip.split(","))

    # Must split the output CSV file into four separate continuous files
    fullList = len(finalList)
    halfList = int(len(finalList) / 2)
    quarterList = int(len(finalList) / 4)
    threeQuarterList = halfList + quarterList

    p1 = multiprocessing.Process(target=firstCSV, args=(quarterList, finalList))
    p2 = multiprocessing.Process(target=secondCSV, args=(quarterList, halfList, finalList))
    p3 = multiprocessing.Process(target=thirdCSV, args=(halfList, threeQuarterList, finalList))
    p4 = multiprocessing.Process(target=fourthCSV, args=(threeQuarterList, fullList, finalList))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

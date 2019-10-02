import sys
import errno
import csv
import os
import multiprocessing

def firstCSV(ip):
    with open('ipblacklist01.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)
                return(row)

def secondCSV(ip):
    with open('ipblacklist02.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)
                return(row)

def thirdCSV(ip):
    with open('ipblacklist03.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)
                return(row)

def fourthCSV(ip):
    with open('ipblacklist04.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)
                return(row)

if __name__ == "__main__":
    infile = input("Text file with list of IP addresses to look up: ")
    ipList = []
    blacklist1 = []
    blacklist2 = []
    blacklist3 = []
    blacklist4 = []

    with open(infile, "r") as f:
        for line in f:
            ipList.append(line.rstrip())

    for ip in ipList:
        blacklist1.append(firstCSV(ip))
        blacklist2.append(secondCSV(ip))
        blacklist3.append(thirdCSV(ip))
        blacklist4.append(fourthCSV(ip))

    with open('realBlacklist01.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for y in range(0, len(blacklist1)):
            if not blacklist1[y] is None:
                writer.writerow(blacklist1[y])
    print("\nGenerated first CSV file...\n")

    with open('realBlacklist02.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for y in range(0, len(blacklist2)):
            if not blacklist2[y] is None:
                writer.writerow(blacklist2[y])
    print("\nGenerated second CSV file...\n")

    with open('realBlacklist03.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for y in range(0, len(blacklist3)):
            if not blacklist3[y] is None:
                writer.writerow(blacklist3[y])
    print("\nGenerated third CSV file...\n")

    with open('realBlacklist04.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Source","IP Address"])
        for y in range(0, len(blacklist4)):
            if not blacklist4[y] is None:
                writer.writerow(blacklist4[y])
    print("\nGenerated fourth CSV file...\n")
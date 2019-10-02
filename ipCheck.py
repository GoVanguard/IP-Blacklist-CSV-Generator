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

def secondCSV(ip):
    with open('ipblacklist02.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)

def thirdCSV(ip):
    with open('ipblacklist03.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)

def fourthCSV(ip):
    with open('ipblacklist04.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if str(ip) in row:
                print("Match!")
                print(row)

if __name__ == "__main__":
    ip = input("IP address to look up: ")

    p1 = multiprocessing.Process(target=firstCSV, args=(ip,))
    p2 = multiprocessing.Process(target=secondCSV, args=(ip,))
    p3 = multiprocessing.Process(target=thirdCSV, args=(ip,))
    p4 = multiprocessing.Process(target=fourthCSV, args=(ip,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

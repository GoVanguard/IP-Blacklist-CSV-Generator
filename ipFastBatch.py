import csv
import errno
import getopt
import os
import sys
import time
from pathlib import Path

if __name__ == "__main__":
    infile = ""

    # Parse arguments
    opts, args = getopt.getopt(sys.argv[1:], "l:", ["list="])
    for opt, arg in opts:
        if (opt == "-l") or (opt == "--list"):
            infile = arg

    # Find all CSV files in the working directory
    filesToProcess = [str(f.name) for f in Path("./").glob("{0}".format("*.csv"))]
    filesToProcessLen = len(filesToProcess)

    if filesToProcessLen > 0:
        print("Found CSV files...")
        print("Building lookup map. Please wait...")
    else:
        print("No CSV files found! Try running ipblacklist.py first. Exiting...")
        sys.exit(1)

    # Load blacklists into a dictionary
    percent = 0
    blocklist_dict = {}
    for fileNameIn in filesToProcess:
        with open(fileNameIn, "r") as blocklist_source:
            reader = csv.reader(blocklist_source)
            for row in reader:
                key = row[1]
                value = row[0]

                # Create new dictionary keys as needed
                if not key in blocklist_dict:
                    blocklist_dict[key] = []

                blocklist_dict[key].append(value)

            percent += 25
            print(percent, "%...", sep='', end='\r')

    # Get the list of IP addresses to test
    if infile == "":
        infile = input("Text file with list of IP addresses to look up: ")
    print("Using input file " + infile)

    # Output a CSV row for each IP found on a blacklist
    with open('output/ipBlacklistResults_'+str(time.time()).split('.')[0]+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["IP Address", "Blacklist Source(s)"])
        with open(infile, "r") as f:
            for line in f:
                line = line.strip()
                if line in blocklist_dict:
                    writer.writerow([line, ', '.join(blocklist_dict[line])])

    print("Done. Check the output folder for your CSV file.")

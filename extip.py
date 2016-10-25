#!/usr/bin/python

# extip.py - Python ip extractor by jakes

# Extract IPs from text file, remove duplicates and 
# output to standard output

# TODO: File output
#       Include file stream buffering to cut down on overhead

import os, sys, re


def printUsage(msg):
    print msg+" :\nUsage :\n\text_ip FILENAME\n\n"

# Check for correct number of arguments on command line
if len(sys.argv) != 2:
    printUsage("\nYour argument(s) is invalid!!")
    sys.exit(1)

# If file is valid, read it and place all IPs in a list
if os.path.isfile(sys.argv[1])!=1: 
    printUsage("\nfile \'"+sys.argv[1]+"\' is not valid")
    sys.exit(1)
else:
    file = open(sys.argv[1],'r')
    fileStr = file.read()
    ipListtmp = re.findall(r'[0-9]+(?:\.[0-9]+){3}', fileStr)

# Remove duplicates * Also scrambles order *
ipList = list(set(ipListtmp))

# Change to customize delimiter
delimiter = "\n"
output = ""

# Output IPs
for ip in ipList:
    output += ip+delimiter

# Print output to STDOUT
print output

# clean up and exit
file.close()
sys.exit(0)


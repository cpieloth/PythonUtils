#!/usr/bin/env python
# Python 3
import re

# Variables
input = 'input.html'	# TODO to set
output = 'output.txt'	# TODO to set
URL = 'url'
TAG = 'tag'
TYPE = URL	# TODO to set
found = 0

# Regex
URLRX = '([http|https]://download[\w\d:#@%/;$()~_?\+-=\\\.&]*)'	# TODO to set
TAGRX = '<FORM ACTION="(http://download.*)" STYLE="display: inline;" TARGET="_blank">'	# TODO to set
regEx = None
if(TYPE == URL):
	regEx = re.compile(URLRX)
if(TYPE == TAG):
	regEx = re.compile(TAGRX)

# Print information
print('Input:', input)
print('Output:', output)
print('Type:', TYPE)

# Filter
try:
	# Open file
	inFile = open(input, 'r')
	outFile = open(output,'w')
	for line in inFile:
		print(".", end="")
		for url in regEx.findall(line):
			print("|", end="")
			found = found + 1
			outFile.write(url)
			outFile.write('\n')	
	print()
	inFile.close()
	outFile.close()
except IOError:
	print("ERROR: IOError, could open or read/write to file!")

print("Found: " + str(found))
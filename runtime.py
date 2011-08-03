#!/usr/bin/env python
# Python 3
import shlex
import subprocess
import re

# Variables
PRG_NAME = 'program.exe'	# TODO to set
DATA_NAME = 'output.csv'	# TODO to set
START = 100	# TODO to set
STEPS = 100	# TODO to set
END = 6000	# TODO to set
RUNS = 5	# TODO to set

# Print information
print('Program:', PRG_NAME)
print('Start size:', START)
print('Step size:', STEPS)
print('End size:', END)
print('Run size:', RUNS)
print('Outputfile: ', DATA_NAME, '\n', sep='')

# Open file
file = open(DATA_NAME, 'w')

# Run tests
print('Start runs:')
size = START
regEx = re.compile('.*time=(.*);.*')

while size <= END:
	# prepare command to start
	command = PRG_NAME + " t g " + str(size) + " 5"	# TODO to set
	print('   command:', command, end=' ')
	args = shlex.split(command)
	avgTime = 0
	
	for run in range(0, RUNS):
		p = subprocess.Popen(args, stdout=subprocess.PIPE)
		p.wait()
		time = regEx.match(str(p.stdout.read()))
		avgTime = avgTime + float(time.group(1))
		print('.', end='')
		
	avgTime = avgTime/RUNS
	print(' size', size, 'done! Average time:', avgTime)
	file.write(str(size*size) + '\t' + str(avgTime) + '\n') # TODO to set
	size = size + STEPS
	
# Close file
file.close()

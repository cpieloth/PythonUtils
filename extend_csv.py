#!/usr/bin/env python
# Python 3
import fileinput

# Variables
DEST_NAME = 'output.csv'	# TODO to set
SRC1_NAME = 'input1.csv'	# TODO to set
SRC2_NAME = 'intput2.csv'	# TODO to set
# Columns start with 0 to n-1
START1_COL = 0	# TODO to set
END1_COL = 1	# TODO to set
START2_COL = 1	# TODO to set
END2_COL = 1	# TODO to set

# Read source files
rows = []
start_col = 0
end_col = 0
fileInput = fileinput.input([SRC1_NAME, SRC2_NAME])
for lines in fileInput:
	# Prepare 2D-Array
	if(fileInput.filename() == SRC1_NAME):
		rows.append([])
	# Set columns to extend
	if(fileInput.isfirstline()):
		if(fileInput.filename() == SRC1_NAME):
			start_col = START1_COL
			end_col = END1_COL
		if(fileInput.filename() == SRC2_NAME):
			start_col = START2_COL
			end_col = END2_COL
			
	# Add columns
	cols = lines.split('\t')
	for i in range(start_col, end_col+1):
		rows[fileInput.filelineno()-1].append(cols[i].rstrip())

# Write destination file
dest_file = open(DEST_NAME, "w")
for row in rows:
	line = ''
	for col in row:
		line = line + col + '\t'
	line = line.rstrip() + '\n'
	dest_file.write(line)
dest_file.close()

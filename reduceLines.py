#!/usr/bin/env python
"""Reduces a file by taking every x line, e.g. to reduce point clouds."""

import argparse

def main():
	# CLI arguments
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input', help='Input log file.')
	parser.add_argument('output', help='Output file. Will be overwritten!')
	parser.add_argument('skip', help='Take every (1), every second (2) ... line.')
	args = parser.parse_args()
	
	# Open file
	file_in = open(args.input, 'r')
	file_out = open(args.output, 'w')
	skip = int(args.skip)
	# Parse file
	count = 1
	for line in file_in:
		if(count == skip):
			file_out.write(line)
			count = 1
		else:
			count = count + 1
	
	# Close file
	file_out.close()
	file_in.close()


if __name__ == "__main__":
	main()

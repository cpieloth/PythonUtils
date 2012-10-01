#!/usr/bin/env python
"""Extracts and sums runtimes from a log file."""

import argparse
import re

class TimeRecord:
	"""Stores all information about a defined time tag, which should be extracted."""
	
	_pattern = ""
	_sum = 0
	_count = 0
	_name = ""
	
	def __init__(self, pattern, name):
		self._pattern = re.compile(pattern)
		self._name = name
		
	@property
	def pattern(self):
		return self._pattern
	
	@pattern.setter
	def pattern(self, value):
		self._pattern = re.compile(value)
		
	def match(self, line):
		m = self._pattern.match(line)
		time = -1
		if m is not None:
			time = float(m.group(1))
		return time
		
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value
		
	@property
	def sum(self):
		return self._sum
	
	def add_time(self, value):
		self._sum += value
		self._count += 1
		
	def get_average(self):
		if(self._count == 0):
			return 0
		return self._sum / self._count
	
	@property
	def count(self):
		return self._count


def main():
	# CLI arguments
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input', help='Input log file.')
	parser.add_argument('output', help='Output file. Will be overwritten!')
	args = parser.parse_args()
	
	# TODO place your regex here to extract the times
	records = []
	records.append(TimeRecord('.*time_foo: (.*)', 'foo(): '))
	records.append(TimeRecord('.*time_bar: (.*)', 'bar(): '))
	records.append(TimeRecord('.*time_baz: (.*)', 'baz(): '))
	
	# Open file
	file_in = open(args.input, 'r')
	file_out = open(args.output, 'w')
	
	# Parse file
	for line in file_in:
		for rec in records:
			time = rec.match(line)
			if 0 < time:
				rec.add_time(time)
	
	# Write results
	for rec in records:
		file_out.write('Count ' + rec.name + str(rec.count) + '\n')
		file_out.write('Time ' + rec.name + str(rec.sum) + '\n')
		file_out.write('Average ' + rec.name + str(rec.get_average()) + '\n')
		file_out.write('\n')
	
	# Close file
	file_out.close()
	file_in.close()


if __name__ == "__main__":
	main()

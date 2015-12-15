import sys
import fileinput
import re
from datetime import datetime

def main(argv):
	line_len = 0
	start = datetime.now()
	
	# Get all lines in the input file
	lines = [line.strip() for line in fileinput.input(argv[0])]

	for line in lines:
		esc_len = len("\"" + re.escape(line) + "\"")
		str_len = len(line)
		line_len += (esc_len - str_len)
	
	print 'Total length difference = ' + str(line_len)

	print (datetime.now() - start)
	

if __name__ == '__main__':
	main(sys.argv[1:])
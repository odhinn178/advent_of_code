import sys
import fileinput
import re

def main(argv):
	total_naughty = 0
	total_nice = 0
	for line in fileinput.input(str(argv[0])):
		if is_nice(line.strip()):
			print 'String ' + line.strip() + ' is nice!!'
			total_nice += 1
		else:
			print 'String ' + line.strip() + ' is naughty!'
			total_naughty += 1
	
	print 'Total nice lines = ' + str(total_nice)


def is_nice(str):
	nice = False
	if re.search(r'([a-z]{2}).*\1', str) and re.search(r'([a-z]).\1', str):
		nice = True
	return nice


if __name__ == '__main__':
	main(sys.argv[1:])
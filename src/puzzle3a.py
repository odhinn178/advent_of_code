import sys


def main(argv):
	with open(str(argv[0]), 'r') as f:
		puzzle_input = f.read()
	
	print 'Total moves = ' + str(len(puzzle_input))

	# Find max dim in each direction
	minmax = find_minmax_xy(puzzle_input)


#def parse_moves(sequence):
	# Create a list with x,y and number of presents


	# Parse the string and record the position for each move
	


def find_minmax_xy(sequence):
	# Create a list for x and y, record each xy position
	x = []
	y = []
	x.append(0)
	y.append(0)
	index = 0
	for m in sequence:
		if m == '<':
			xd = x[index] - 1
		elif m == '>':
			xd = x[index] + 1
		elif m == 'v':
			yd = y[index] - 1
		elif m == '^':
			yd = y[index] + 1
		x.append(xd)
		y.append(yd)
		index += 1
	xmin = min(x)
	xmax = max(x)
	ymin = min(y)
	ymax = max(y)
	print 'xmin = ' + str(xmin) + ', xmax = ' + str(xmax) + ', ymin = ' + str(ymin) + ', ymax = ' + str(ymax)
	minmax = [xmin, xmax, ymin, ymax]


if __name__ == '__main__':
	main(sys.argv[1:])
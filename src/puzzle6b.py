import sys
import fileinput
import numpy as np
import re
from datetime import datetime

def main(argv):
	start = datetime.now()
	# Create the grid
	light_grid = np.zeros([1000, 1000], dtype=np.int)
	for line in fileinput.input(str(argv[0])):
		coords = find_coords(line.strip())

		# Iterate over the range of light positions to change
		for x in range(coords[0][0], coords[1][0]+1):
			for y in range(coords[0][1], coords[1][1]+1):
				if re.match('turn on', line):
					light_grid[x][y] += 1
				elif re.match('turn off', line):
					if light_grid[x][y] > 0:
						light_grid[x][y] -= 1
				elif re.match('toggle', line):
					light_grid[x][y] += 2

	total_b = total_bright(light_grid)
	print 'Total brightness = ' + str(total_b)

	print (datetime.now() - start)
	

def find_coords(str):
	# Search the string for the coordinates
	c_group = re.findall('(\d+,\d+)', str)
	c_start = c_group[0].split(',')
	c_stop = c_group[1].split(',')
	c = [[int(c_start[0]), int(c_start[1])], [int(c_stop[0]), int(c_stop[1])]]
	return c


def total_bright(grid):
	# Flatten the grid and find total brightness
	b_total = 0
	l_array = grid.flatten()
	b_count = np.bincount(l_array)
	# At this point we have a list of bins with count values
	for x in range(0,b_count.size):
		b_total += b_count[x] * x
	return b_total


if __name__ == '__main__':
	main(sys.argv[1:])
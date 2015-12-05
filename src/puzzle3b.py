import sys
import numpy as np

def main(argv):
	with open(str(argv[0]), 'r') as f:
		moves = f.read()
	
	print 'Total moves = ' + str(len(moves))

	# Find max dim in each direction
	minmax = find_minmax_xy(moves)

	# Allocate a grid based on minmax results
	grid_max = max([minmax[2], minmax[5]])
	print 'grid_max = ' + str(grid_max)
	house_data = np.zeros([grid_max * 2, grid_max * 2], dtype=np.int)

	# Set initial position as map center
	xs = ys = grid_max
	xr = yr = grid_max

	# Initial position house gets a present
	house_data[xs][ys] = 1

	# For each entry in the sequence, parse the entry and calc delta
	for i, m in enumerate(moves):
		delta = parse_move(m)
		#print 'delta_xy = ' + str(delta[0]) + ',' + str(delta[1])
		if (i % 2) == 0:
			xr += delta[0]
			yr += delta[1]
			house_data[xr][yr] = 1
		else:
			xs += delta[0]
			ys += delta[1]
			house_data[xs][ys] = 1
		#print 'xy = ' + str(x) + ',' + str(y)

	# Find the number of houses that got at least one present
	house_array = house_data.flatten()
	house_count = np.bincount(house_array)
	print 'Happy houses = ' + str(house_count[1]) + ', sad houses = ' + str(house_count[0])


def parse_move(m_input):
	# Interpret move and return 
	xd = 0
	yd = 0
	if m_input == '<':
		xd = -1
	elif m_input == '>':
		xd = 1
	elif m_input == 'v':
		yd = -1
	elif m_input == '^':
		yd = 1
	delta = [xd, yd]
	return delta


def find_minmax_xy(sequence):
	# Find the min and max (x,y)
	x = 0
	y = 0
	xmin = 0
	xmax = 0
	ymin = 0
	ymax = 0
	for m in sequence:
		if m == '<':
			x -= 1
			if x < xmin:
				xmin = x
		elif m == '>':
			x += 1
			if x > xmax:
				xmax = x
		elif m == 'v':
			y -= 1
			if y < ymin:
				ymin = y
		elif m == '^':
			y += 1
			if y > ymax:
				ymax = y
	print 'xmin = ' + str(xmin) + ', xmax = ' + str(xmax) + ', ymin = ' + str(ymin) + ', ymax = ' + str(ymax)
	x_range = (xmax - xmin)
	y_range = (ymax - ymin)
	print 'x_range = ' + str(x_range) + ', y_range = ' + str(y_range)
	minmax = [xmin, xmax, x_range, ymin, ymax, y_range]
	return minmax


if __name__ == '__main__':
	main(sys.argv[1:])
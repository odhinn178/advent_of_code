import sys
import fileinput

def main(argv):
	total_sqft = 0
	total_ribbon = 0
	
	for line in fileinput.input(str(argv[0])):
		dims_text = line.strip().split('x')
		dims = [int(x) for x in dims_text]
		sqft = calc_sqft(dims)
		total_sqft += sqft
		ribbon = calc_ribbon(dims)
		total_ribbon += ribbon
	
	print "Total sqft = " + str(total_sqft)
	print "Total ribbon = " + str(total_ribbon)


def calc_sqft(dims):
	paper = (2*dims[0]*dims[1]) + (2*dims[1]*dims[2]) + (2*dims[2]*dims[0])
	dims.sort()
	slack = dims[0] * dims[1]
	return (paper + slack)


def calc_ribbon(dims):
	dims.sort()
	perim = (2*dims[0]) + (2*dims[1])
	bow = (dims[0] * dims[1] * dims[2])
	return (perim + bow)


if __name__ == "__main__":
    main(sys.argv[1:])
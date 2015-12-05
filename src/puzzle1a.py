import sys

def main(argv):
	floor_val = 0
	got_first_basement = False

	with open(str(argv[0]), 'r') as f:
		file_data = f.read()

	for i, c in enumerate(file_data):
		if c == '(':
			floor_val += 1
		elif c == ')':
			floor_val -= 1
		if got_first_basement is False and floor_val == -1:
			print 'First position in basement: ', i + 1
			got_first_basement = True

	print 'Final floor value: ', floor_val


if __name__ == "__main__":
    main(sys.argv[1:])
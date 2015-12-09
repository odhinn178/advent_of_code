import sys
import re
from datetime import datetime


def main(argv):
	new_lines = []
	start = datetime.now()

	f = open(argv[0], "r")
	lines = [line.strip() for line in f]
	f.close()

	# Use a dictionary for wire names
	wires = dict()
	temp_list = []
	wire_list = []

	# Create a list of wire names from the output of the assignments
	match_wire = re.compile(r'.*-> ([a-z]+)$')
	for line in lines:
		res = match_wire.search(line)
		temp_list.append(res.groups()[0])

	temp_set = set(temp_list)
	wire_list = list(temp_set)

	# Then create a dictionary of wires
	for wire in wire_list:
		wires[wire] = None

	# Iterate through the lines of the sorted output, performing logic operations
	# For each output assignment, check that one or both inputs are present
	while wires['a'] == None:
		for line in lines:
			#print line
			out_res = re.search(r'.*-> ([a-z]+)$', line)
			out_wire = out_res.groups()[0]
			#print 'out_wire = ' + out_wire
			cmd_res = re.search(r'([A-Z]+)', line)
			if cmd_res:
				cmd = cmd_res.groups()[0]
				#print 'command = ' + cmd
				# This is an operation, get the second operand and the first if the command isn't NOT
				op2_res = re.search(r'([0-9a-z]+) ->', line)
				op2 = op2_res.groups()[0]
				#print 'op2 = ' + op2
				if cmd != 'NOT':
					op1_res = re.match(r'([0-9a-z]+)', line)
					op1 = op1_res.groups()[0]
					#print 'op1 = ' + op1
					if cmd == 'AND':
						if not is_number(op1) and not is_number(op2):
							if (wires[op1] is not None) and (wires[op2] is not None):
								wires[out_wire] = wires[op1] & wires[op2]
						elif is_number(op1) and not is_number(op2):
							if wires[op2] is not None:
								wires[out_wire] = int(op1) & wires[op2]
						elif not is_number(op1) and is_number(op2):
							if wires[op1] is not None:
								wires[out_wire] = wires[op1] & int(op2)
						else:
							wires[out_wire] = int(op1) & int(op2)
					elif cmd == 'OR':
						if not is_number(op1) and not is_number(op2):
							if (wires[op1] is not None) and (wires[op2] is not None):
								wires[out_wire] = wires[op1] | wires[op2]
						elif is_number(op1) and not is_number(op2):
							if wires[op2] is not None:
								wires[out_wire] = int(op1) | wires[op2]
						elif not is_number(op1) and is_number(op2):
							if wires[op1] is not None:
								wires[out_wire] = wires[op1] | int(op2)
						else:
							wires[out_wire] = int(op1) & int(op2)
					elif cmd == 'RSHIFT':
						# Second operand is always a number
						if wires[op1] is not None:
							wires[out_wire] = wires[op1] >> int(op2)
					elif cmd == 'LSHIFT':
						# Second operand is always a number
						if wires[op1] is not None:
							wires[out_wire] = (wires[op1] << int(op2)) & 0xFFFF
				else:
					# Command is NOT
					if wires[op2] is not None:
						wires[out_wire] = (~wires[op2]) & 0xFFFF
			else:
				# This is an assignment operation
				op_res = re.match(r'([0-9a-z]+)', line)
				op = op_res.groups()[0]
				#print 'op = ' + op
				if is_number(op):
					wires[out_wire] = int(op)
				else:
					if wires[op] is not None:
						wires[out_wire] = wires[op]
	
	# Finally, present the output of signal 'a'
	print 'Final value of a = ' + str(wires['a'])

	# Override b with signal on a
	wire_b = wires['a']

	# Reset everything else
	for wire in wire_list:
		wires[wire] = None

	# Reassign to b
	wires['b'] = wire_b

	# Re-run but don't allow assignment to b
	while wires['a'] == None:
		for line in lines:
			#print line
			out_res = re.search(r'.*-> ([a-z]+)$', line)
			out_wire = out_res.groups()[0]
			if out_wire == 'b':
				continue
			else:
				#print 'out_wire = ' + out_wire
				cmd_res = re.search(r'([A-Z]+)', line)
				if cmd_res:
					cmd = cmd_res.groups()[0]
					#print 'command = ' + cmd
					# This is an operation, get the second operand and the first if the command isn't NOT
					op2_res = re.search(r'([0-9a-z]+) ->', line)
					op2 = op2_res.groups()[0]
					#print 'op2 = ' + op2
					if cmd != 'NOT':
						op1_res = re.match(r'([0-9a-z]+)', line)
						op1 = op1_res.groups()[0]
						#print 'op1 = ' + op1
						if cmd == 'AND':
							if not is_number(op1) and not is_number(op2):
								if (wires[op1] is not None) and (wires[op2] is not None):
									wires[out_wire] = wires[op1] & wires[op2]
							elif is_number(op1) and not is_number(op2):
								if wires[op2] is not None:
									wires[out_wire] = int(op1) & wires[op2]
							elif not is_number(op1) and is_number(op2):
								if wires[op1] is not None:
									wires[out_wire] = wires[op1] & int(op2)
							else:
								wires[out_wire] = int(op1) & int(op2)
						elif cmd == 'OR':
							if not is_number(op1) and not is_number(op2):
								if (wires[op1] is not None) and (wires[op2] is not None):
									wires[out_wire] = wires[op1] | wires[op2]
							elif is_number(op1) and not is_number(op2):
								if wires[op2] is not None:
									wires[out_wire] = int(op1) | wires[op2]
							elif not is_number(op1) and is_number(op2):
								if wires[op1] is not None:
									wires[out_wire] = wires[op1] | int(op2)
							else:
								wires[out_wire] = int(op1) & int(op2)
						elif cmd == 'RSHIFT':
							# Second operand is always a number
							if wires[op1] is not None:
								wires[out_wire] = wires[op1] >> int(op2)
						elif cmd == 'LSHIFT':
							# Second operand is always a number
							if wires[op1] is not None:
								wires[out_wire] = (wires[op1] << int(op2)) & 0xFFFF
					else:
						# Command is NOT
						if wires[op2] is not None:
							wires[out_wire] = (~wires[op2]) & 0xFFFF
				else:
					# This is an assignment operation
					op_res = re.match(r'([0-9a-z]+)', line)
					op = op_res.groups()[0]
					#print 'op = ' + op
					if is_number(op):
						wires[out_wire] = int(op)
					else:
						if wires[op] is not None:
							wires[out_wire] = wires[op]

	# Finally, present the output of signal 'a'
	print 'Final value of a, part 2 = ' + str(wires['a'])

	print (datetime.now() - start)
	

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


if __name__ == '__main__':
	main(sys.argv[1:])
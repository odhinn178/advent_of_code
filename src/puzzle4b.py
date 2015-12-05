import sys
import hashlib

def main(argv):
	key = argv[0]
	print 'Secret key = ' + key

	# Perform hashes and look for first value with 5 leading hex zeros
	hash_found = False
	hash_int = 0
	while not hash_found:
		hash_str = key + str(hash_int)
		hash_parse = hashlib.md5()
		hash_parse.update(hash_str)
		hash_result = hash_parse.hexdigest()
		#print 'hash of ' + hash_str + ' = ' + hash_result
		hash_top = hash_result[0:6]
		if int(hash_top, 16) == 0:
			hash_found = True
			print 'Success! hash_int = ' + str(hash_int)
			print 'hash of ' + hash_str + ' = ' + hash_result
		else:
			hash_int += 1


if __name__ == '__main__':
	main(sys.argv[1:])
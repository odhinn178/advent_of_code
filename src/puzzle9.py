import sys
import fileinput
from datetime import datetime
from itertools import permutations

def main(argv):
    cities = set()
    distances = dict()

    start = datetime.now()
	
    # Get all sets of cities and distances
    lines = [line.strip() for line in fileinput.input(argv[0])]
    for line in lines:
        (src, _, dest, _, dist) = line.split()
        cities.add(src)
        cities.add(dest)
        distances.setdefault(src, dict())[dest] = int(dist)
        distances.setdefault(dest, dict())[src] = int(dist)

    min_dist = sys.maxsize
    max_dist = 0

    for items in permutations(cities):
        dist = sum(map(lambda x,y: distances[x][y], items[:-1], items[1:]))
        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)

    print 'minimum distance = ' + str(min_dist)
    print 'maximum distance = ' + str(max_dist)
	
    print (datetime.now() - start)
	

if __name__ == '__main__':
    main(sys.argv[1:])
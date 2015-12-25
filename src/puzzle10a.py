import re
from datetime import datetime

input = '3113322113'
max_iter = 40

def main():
    index = 0
    output = ''
    start = datetime.now()

    # Iterate over the input sequence
    for i in range(max_iter):
        match = re.match('[0-9]+', input[index:])



    print (datetime.now() - start)


if __name__ == '__main__':
    main()
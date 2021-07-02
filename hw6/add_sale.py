import sys

def sums(num):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{num}\n')

sums(sys.argv[1])
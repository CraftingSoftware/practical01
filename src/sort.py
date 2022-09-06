

args = sys.argv
numbers = list(map(int, args))
numbers.sort()
for number, index in enumerate(numbers):
    print(f'[{index}] {number}')

filename = 'C:/Users/And/Desktop/wot/numbers.txt'
output = 'C:/Users/And/Desktop/wot/output.txt'


with open(filename) as f:
    _min = _max = float(f.readline())
    for line in f:
        num = float(line)
        if num > _max:
            _max = num
        if num < _min:
            _min = num

    _sum = _max + _min

with open(output, 'w') as f:
    f.write(str(_sum))
    f.write('\n')
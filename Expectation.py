def expected_value(line):
    number = line.split()
    couples = {}
    couples['0'] = 1
    couples['1'] = 1
    couples['2'] = 1
    couples['3'] = 0.75
    couples['4'] = 0.5
    couples['5'] = 0

    ExValue = 0

    for k in range(len(number)):
        ExValue += couples[f'{k}'] * 2 * int(number[k])
    return ExValue

print(expected_value(input('Enter the number of different allels: \n')))
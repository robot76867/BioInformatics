def expected_value(line):
    number = line.split()
    couples = {}
    couples['0'] = 1 # AA-AA
    couples['1'] = 1 # AA-Aa
    couples['2'] = 1 # AA-aa
    couples['3'] = 0.75 #Aa-Aa
    couples['4'] = 0.5 #Aa-aa
    couples['5'] = 0 #aa-aa

    ExValue = 0

    for k in range(len(number)):
        ExValue += couples[f'{k}'] * 2 * int(number[k])
    return ExValue

print(expected_value(input('Enter the number of different allels: \n')))

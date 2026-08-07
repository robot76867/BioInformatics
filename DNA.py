with open('DNA.txt', 'r') as file:
    new_stroke = ''
    while True:
        char = file.read(1)
        if not char:
            print(f'Complemented DNA: \n{new_stroke[::-1]}')
            break
        if char == 'A':
            new_stroke += char.replace('A', 'T')
        elif char == 'T':
            new_stroke += char.replace('T', 'A')
        elif char == 'C':
            new_stroke += char.replace('C', 'G')
        else:
            new_stroke += char.replace('G', 'C')

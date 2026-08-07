#HAMMING

with open('Hamming.txt', 'r') as file:
    strokes = file.readlines()
    line1 = strokes[0].strip()
    line2 = strokes[1].strip()
    counter = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            counter += 1
    print(f'The overall Hamming distance: {counter}')



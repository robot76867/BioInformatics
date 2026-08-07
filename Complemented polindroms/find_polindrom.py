import time

start_time = time.time()
with open('ProteinPol.txt', 'r') as file:
    strokes = file.readlines()
    main_DNA = ''

    for stroke in strokes:
        if stroke.startswith('>') or not stroke:
            pass
        else:
            main_DNA += stroke.strip()

    for i in range(0, len(main_DNA)+1, 2):
        for j in range(0, len(main_DNA)+1, 2):


            if j >= i and i <= (j - 3):

                codon = main_DNA[i:j]

                compCodon = ''
                start = i+1
                for char in codon:
                    if char == 'A':
                        compCodon += char.replace('A', 'T')
                    elif char == 'T':
                        compCodon += char.replace('T', 'A')
                    elif char == 'C':
                        compCodon += char.replace('C', 'G')
                    else:
                        compCodon += char.replace('G', 'C')
                revCodon = compCodon[::-1]

                if revCodon == codon:
                    print(start, len(codon))
end_time = time.time()
print(end_time-start_time)

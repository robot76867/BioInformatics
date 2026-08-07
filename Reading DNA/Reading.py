alphabetForDNA = {
    'TTT' : 'F', 'TTC' : 'F',
    'TTA' : 'L', 'TTG' : 'L', 'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L',
    'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I',
    'ATG' : 'M',
    'GTT' : 'V', 'GTC' : 'V', 'GTA' : 'V', 'GTG' : 'V',
    'TCT' : 'S', 'TCC' : 'S', 'TCA' : 'S', 'TCG' : 'S', 'AGT' : 'S', 'AGC' : 'S',
    'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
    'ACT' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
    'GCT' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
    'TAT' : 'Y', 'TAC' : 'Y',
    'CAT' : 'H', 'CAC' : 'H',
    'CAA' : 'Q', 'CAG' : 'Q',
    'AAT' : 'N', 'AAC' : 'N',
    'AAA' : 'K', 'AAG' : 'K',
    'GAT' : 'D', 'GAC' : 'D',
    'GAA' : 'E', 'GAG' : 'E',
    'TGT' : 'C', 'TGC' : 'C',
    'TGG' : 'W',
    'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGA' : 'R', 'AGG' : 'R',
    'GGT' : 'G', 'GGC' : 'G', 'GGA' :  'G', 'GGG' : 'G',
    'TAA' : 'STOP', 'TAG' : 'STOP', 'TGA' : 'STOP'}

def translationDNA(filename):
    all_strings = []
    DNA_stroke = ''
    comp_stroke = ''
    with open(f'{filename}', 'r') as file:
        strokes = file.readlines()
        for i in range(len(strokes)):
            stroke = strokes[i]

            if stroke.startswith('>'):
                pass
            else:
                DNA_stroke += stroke.strip()

    for char in DNA_stroke:
        if not char:
            break
        elif char == 'A':
            comp_stroke += char.replace('A', 'T')
        elif char == 'T':
            comp_stroke += char.replace('T', 'A')
        elif char == 'C':
            comp_stroke += char.replace('C', 'G')
        elif char == 'G':
            comp_stroke += char.replace('G', 'C')
    compDNA = comp_stroke[::-1]

    line = ''
    for i in range(len(DNA_stroke)):
        codon = DNA_stroke[i:i+3]
        amino_acid = alphabetForDNA.get(codon)

        if not amino_acid:
            break

        if amino_acid == 'M' and line == '':
            line += amino_acid
            for j in range(i+3, len(DNA_stroke), 3):
                subCodon = DNA_stroke[j:j+3]
                subAcid = alphabetForDNA.get(subCodon)
                if not subAcid:
                    break
                if subAcid == 'STOP':
                    all_strings.append(line)
                    line = ''
                    break
                elif subAcid != 'STOP':
                    line += subAcid

    compLine = ''

    for u in range(len(compDNA)):
        compCodon = compDNA[u:u+3]
        compAcid = alphabetForDNA.get(compCodon)

        if not compAcid:
            break

        if compAcid == 'M' and compLine == '':
            compLine += compAcid
            for t in range(u+3, len(compDNA), 3):
                subCompCodon = compDNA[t:t+3]
                subCompAcid = alphabetForDNA.get(subCompCodon)
                if not subCompAcid:
                    break
                if subCompAcid == 'STOP':
                    all_strings.append(compLine)
                    compLine = ''
                    break
                elif subCompAcid != 'STOP':
                    compLine += subCompAcid
    all_strings_fixed = list(set(all_strings))
    print('Total variables to read DNA:')
    for h in range(len(all_strings_fixed)):
        print(all_strings_fixed[h])



translationDNA('ReadDna.txt')

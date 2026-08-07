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
    'TAA' : 'stop', 'TAG' : 'stop', 'TGA' : 'stop'}

line = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

print(line[6::].index('T'))
pr = ''
for i in range(0, len(line)):
    acid = alphabetForDNA.get(line[i:i+3])
    if acid == 'M':
        pr += acid
        for k in range(0, len(line[i+3:]), 3):
            dick = alphabetForDNA.get(line[i:i+3])
            if dick != 'stop' and dick != 'M':
                pr += dick
            if not dick or dick == 'stop':
                break
    elif acid != 'STOP' and acid:
        pr += acid
    else:
        break
print(pr)
print(len(line[2::]))
# new = ''
# rev = line[::-1]
#
# for char in line:
#     if not char:
#         print(new[::-1])
#         break
#     if char == 'A':
#         new += char.replace('A', 'T')
#     elif char == 'T':
#         new += char.replace('T', 'A')
#     elif char == 'C':
#         new += char.replace('C', 'G')
#     else:
#         new += char.replace('G', 'C')
#
# nnew = new[::-1]
# tr = ''
# op = ''
# print(nnew)
# for r in range(0, len(new), 3):
#     op += alphabetForDNA.get(new[r:r+3])
# print(op)
#
# for t in range(0, len(nnew), 3):
#     tr += alphabetForDNA.get(nnew[t:t+3])
# print(tr)


proteins = {
    'F' : 2, # Fenilalanine
    'L' : 6, # Leycin
    'I' : 3, # Isoleycin
    'M' : 1, # Metionine
    'V' : 4, # Valin
    'S' : 6, # Serine
    'P' : 4, # Proline
    'T' : 4, # Trionine
    'A' : 4, # Alanine
    'Y' : 2, # Tirozyn
    'H' : 2, # Histidine
    'Q' : 2, # Glutamine
    'N' : 2, # Asparagine
    'K' : 2, # Lizin
    'D' : 2, # Asparagine acid
    'E' : 2, # Glutamine acid
    'C' : 2, # Cistein
    'W' : 1, # Triptophane
    'R' : 6, # Arginine
    'G' : 4 # Glicin
}

def combinatorika(filename):
    with open(f'{filename}.txt', 'r') as file:
        lines = file.read()
        combinations = 1
        mod = 10 ** 6
        for i in range(len(lines)):
            combinations *= (proteins[f'{lines[i]}'] % mod)
        return combinations * 3 % mod

print(combinatorika('gen'))

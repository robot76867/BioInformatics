def longestSubstring(filename):
    with open(f'{filename}.txt', 'r') as input_file, \
        open('fixed.txt', 'w') as output_file:
        stroke = input_file.readlines()
        genom = ''
        for t in range(len(stroke)):
            if t != 0:
                if stroke[t].startswith('>'):
                    output_file.write(genom + '\n')
                    genom = ''
                    pass
                else:
                    genom += stroke[t].strip()
        output_file.write(genom)
    with open('fixed.txt', 'r') as fixed:
        Long_motif = ''
        lines = fixed.readlines()
        firstLine = lines[0].strip()
        secondLine = lines[1].strip()
        max_combo = 0
        cur_combo = 0
        longLine = ''
        longestSharedMotif = []
        for i in range(len(firstLine)):
            for j in range(i, len(firstLine)):
                if firstLine.find(secondLine[i:j]) != -1 and firstLine.find(secondLine[i:j+1]) != -1:
                    cur_combo += 1
                    longLine += secondLine[j]
                else:
                    if cur_combo >= max_combo:
                        max_combo = cur_combo
                        cur_combo = 0
                        longestSharedMotif.append(longLine)
                        longLine = ''
                        break
                    else:
                        cur_combo = 0
                        longLine = ''
                        break
        for u in range(len(longestSharedMotif)):
            checkMotif = longestSharedMotif[u]
            for l in range(len(lines)):
                checkLine = lines[l]
                if checkLine.find(checkMotif) != -1:
                    pass
                else:
                    longestSharedMotif[u] = ''
                    break

        max_motif = ''
        for y in range(len(longestSharedMotif)):
            curr_motif = longestSharedMotif[y]
            if len(Long_motif) > len(curr_motif):
                pass
            else:
                Long_motif = curr_motif
        return Long_motif

print(longestSubstring('Shared_motifs'))


def overlarping(filename):
    with open(f'{filename}.txt', 'r') as file:
        strokes = file.readlines()
        pairs = []
        names = []
        lines = []
        i = 0

        while i < len(strokes):
            names.append(strokes[i].strip('>').strip())
            lines.append(strokes[i+1].strip() + strokes[i+2].strip())
            i += 3
        for j in range(len(names)):
            for t in range(len(names)):
                curr_name = names[j]
                tail = lines[j][len(lines[j])-3:len(lines[j])]
                pair_name = names[t]
                head = lines[t][:3]
                if tail == head and pair_name != curr_name:
                    pairs.append(curr_name + ' ' + pair_name)
        for n in range(len(pairs)):
            print(pairs[n], end='\n')


overlarping('Graphs')

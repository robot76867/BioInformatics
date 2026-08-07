with open('DNA.txt', 'r') as file:
    strokes = file.readlines()
    counter = 0
    final_stroke = ''
    GC_count = 0
    curr_GC = 0
    max_GC = 0
    all_DNA = 0
    curr_title = ''
    old_title = ''
    max_title = ''
    for i in range(len(strokes)):
        line = strokes[i].strip()
        if line.startswith('>'):
            if curr_title != '' and final_stroke != '':
                all_DNA = len(final_stroke)
                GC_count = final_stroke.count('G') + final_stroke.count('C')
                curr_GC = round(GC_count / all_DNA * 100, 6)
                if curr_GC > max_GC:
                    max_GC = curr_GC
                    max_title = curr_title
            final_stroke = ''
            curr_title = line
        else:
            final_stroke += line
    print(max_title, max_GC, sep='\n')

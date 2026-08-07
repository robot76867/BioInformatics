letters = input('Enter the letters: ').split()
n = int(input('Enter the number of elements in groups: '))
res = []
line = ''
def lexf(arr, depth):
    global line
    if len(line) == depth:
        res.append(line)
        return line

    for char in arr:
        line += char
        lexf(letters, depth)
        line = line[:len(line)-1]


lexf(letters, n)
with open('result.txt', 'w') as file:
    file.write('\n'.join(res))

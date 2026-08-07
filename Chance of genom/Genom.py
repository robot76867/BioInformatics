k = int(input('Enter the number of generation: '))
n = int(input('Enter the number of "Toms" you need: '))
def chanceOfGenom(k, n):
    childs = 2**k
    resultChance = 0
    for i in range(n, childs+1):
        facChilds = 1
        facN = 1
        facRazn = 1
        Razn = childs - i
        for j in range(1, i+1):
            facN = facN * j
        for k in range(1, childs+1):
            facChilds = facChilds * k
        for t in range(1, Razn+1):
            facRazn = facRazn * t
        currChance = facChilds/(facN * facRazn) * pow(0.25, i) * pow(0.75, Razn)
        resultChance += currChance
    return resultChance

print(f'Chance that in {k}th generation could be {n} "Toms" is {chanceOfGenom(k, n):.4f}')

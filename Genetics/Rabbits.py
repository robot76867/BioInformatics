#WITHOUT DEATH

# def rabbits(n, m):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n <= 0:
#         return 0
#     return rabbits(n-1, m) + rabbits(n-2, m) - rabbits(n-m, m)
#
# print(rabbits(89, 16))

#WITH DEATH

def rabbits_dying(n, m):
    ages = [0] * m
    ages[0] = 1

    for month in range(2, n+1):
        new_babies = sum(ages[1:])
        next_ages = [0] * m
        next_ages[0] = new_babies
        next_ages[1:] = ages[:-1]
        ages = next_ages
    return sum(ages)

print(rabbits_dying(99, 17))

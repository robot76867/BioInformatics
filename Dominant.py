k = int(input('Enter the number of homozygotes with dominant trait: '))
m = int(input('Enter the number of heterozygotes: '))
n = int(input('Enter the number of homozygotes with recessive trait: '))

all = k + m + n

m_m = round(m/all * (m-1)/(all-1), 3) * 0.25
print(f'm_m: {m_m}')
n_n = round(n/all * (n-1)/(all-1), 3)
print(f'n_n: {n_n}')
m_n = round(n/all * m/(all-1) + m/all * n/(all-1), 3) * 0.5
print(f'm_n: {m_n}')

P_AA = 1 - m_m - n_n - m_n

print(f'The overall probability that the offspring will exhibit at least one dominant trait: {P_AA:.5f}')
year = 2026
month = 12
days = 12
print(year, month, days, sep='/')
print(f'{days}/{month}/{year}')
print('/'.join([year, month, days]))
print('/'.join([year, month, days]))
print('{2}/{}/{0}'.format(year, month, days))
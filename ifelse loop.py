students = {
    'Ram' : 76,
    'Sita' : 44,
    'Hari' : 91,
    'Gita' : 33

}

for name,marks in students.items():
    if marks>44:
        print(f'{name} : {marks}')
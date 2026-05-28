file_name = ['loop.py','photo.rpg', 'xyz.exe','abc.exe']
new_file = []
for name in file_name:
    if name.endswith('.py'):
        new_file.append(name)
print(new_file)



items = [1, 2, 3, 11.2, 2+4, 'mild', 'apple']

integers = []
floats = []
strings = []

for item in items:
    if type(item) == int:
        integers.append(item)
    elif type(item) == float:
        floats.append(item)
    elif type(item) == str:
        strings.append(item)

print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)

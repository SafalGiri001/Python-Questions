cart = ['milk','milk','apple','orange','orange']
new_file= {}
for i in cart :
    if i in new_file:
        new_file[i] = new_file[i] + 1
    else:
        new_file[i] = 1
print(new_file)

#OR

cart = ['milk','milk','apple','orange','orange']
new_file= {}
for i in cart :
    new_file[i] = new_file.get(i, 0) + 1
print(new_file)



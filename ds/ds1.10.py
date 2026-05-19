lst = [10, 20, 30]
tpl = (10, 20, 30)
st = {40, 50, 60}
d = {'a': 1, 'b': 2}

val = 20

if val in lst and val in tpl:
    if 'b' in d and val not in st:
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")
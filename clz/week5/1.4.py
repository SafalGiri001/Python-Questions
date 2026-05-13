month = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}

values_list = []
for value in month.values():
    if value not in values_list:
        values_list.append(value)

print(values_list)
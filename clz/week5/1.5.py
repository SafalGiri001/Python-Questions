sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = []

for num in sample_list:
    if num not in unique_list:
        unique_list.append(num)

result_tuple = tuple(unique_list)

print("Tuple without duplicates:", result_tuple)
print("Minimum:", min(result_tuple))
print("Maximum:", max(result_tuple))
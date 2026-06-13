#q7
ratings = ['4+','5+','7+','5+','4+']
current_ratings = {}
i = 0
while i < len(ratings):
    current_ratings[ratings[i]] = current_ratings.get(ratings[i], 0) + 1
    i += 1
print(current_ratings)



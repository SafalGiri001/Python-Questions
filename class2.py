rating = ['4+', '9+', '12+', '17+', '4+', '12+', '9+', '17+', '12+', '4+','17+']
content_rating={}
i = 0
while i<len(rating):
    content_rating[rating[i]]=content_rating.get[rating[i],0]+1
    i = i +1
print(content_rating)

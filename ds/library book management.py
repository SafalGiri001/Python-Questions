book = [{'title':'Python','author':'Guido Van Rossum'}]
print('1. Add user')
print('2. Show record')
print('3. Modify record')
print('4. Delete record')
print('5. Exit')
for i in range(3):
    user_choice = int(input("enter any choice(1-5):  "))
    if user_choice == 1:
        title = input("enter book title: ").title()
        author = input("enter book author: ").title()
        book.append({'title':title,'author':author})
        print(book)
    elif user_choice == 2:
        for index, b in enumerate(book):
           print(index,book)
    elif user_choice == 3:
        index_no = int(input("enter index number"))
        if index_no <0 or index_no >= len(book):
            title = input("enter book title: ").title()
            author = input("enter book author: ").title()
            book[i]['title'] = title
            book[i]['author'] = author
            print(book)
    elif user_choice == 4:
        index_no = int(input("enter index number"))
        if index_no <0 or index_no >= len(book):
           book.pop([index_no])
           print(book)
    elif user_choice == 5:
        break
    else:
        print("invalid choice")
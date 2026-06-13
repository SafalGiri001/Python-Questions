user_list = ['ram','hari']
for i in range(3):
    print('1. Add user')
    print('2. Store record')
    print('3. Modify record')
    print('4. Delete record')
    print('5. Exit')
for i in range(3):
    user_choice = input('Enter your choice: ')
    if user_choice == '1':
        user_list.append('sita')
        print(user_list)
    elif user_choice == '2':
        for index_no, user in enumerate(user_list):
            print(index_no,user)
    elif user_choice == '3':
        index_number = int(input('Enter index: '))
        if index_number<0 or index_number >=len(user_list):
            print('Invalid index number')
        else:
            user_list[index_number] = 'sita'
    elif user_choice == '4':
        index_number = int(input('Enter index: '))
        if index_number<0 or index_number >len(user_list):
            print('Invalid index number')
        else:
            user_list.pop(index_number)
    elif user_choice == '5':
        break

password = input('Enter password: ')
attempt =0
for i in range(3):
    re_enter = input("Enter your password: ", )
    if re_enter != password:
        attempt += 1
    elif attempt == 3:
        print('Maximum attempt reached
        break